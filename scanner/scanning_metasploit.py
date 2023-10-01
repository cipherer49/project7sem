import pyshark

# Define the network interface to capture traffic (e.g., 'Wi-Fi' on Windows)
interface = 'Wi-Fi'  # Change this to match your Wi-Fi interface name

# Define the IP address to filter
target_ip = '192.168.1.207'  # Change this to the IP you want to filter

# Create a packet capture object
capture = pyshark.LiveCapture(interface)

try:
    print(f"Capturing live traffic for IP {target_ip}. Press Ctrl+C to stop...")

    # Start capturing packets
    for packet in capture.sniff_continuously():
        try:
            if 'IP' in packet and 'ip.src' in packet and packet['IP'].src == target_ip:
                # Print packet information for the specified source IP
                print(packet)
        except AttributeError:
            pass  # Ignore packets that don't have the expected structure

except KeyboardInterrupt:
    print("Capture stopped by user.")

finally:
    capture.close()