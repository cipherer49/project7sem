import pyshark
import time

# Network interface to capture traffic from on your Windows machine (e.g., "Ethernet")
networkInterface = "Wi-Fi"
# testt ip
ip = "72.163.4.185"

# IP address of your Kali Linux VM
kali_vm_ip = "192.168.191.51"  # Replace with your Kali VM's IP address

# Define your filter expression to capture traffic to/from your Kali VM
filter_expression = f"host {kali_vm_ip}"
filter_expression2 = f"host {ip}"


capture = pyshark.LiveCapture(interface=networkInterface, bpf_filter=filter_expression and filter_expression2)
print(f"Listening on {networkInterface} with filter: {filter_expression}")

# Dictionary to track unique connection attempts
connection_attempts = {}

for packet in capture.sniff_continuously():
    try:
        localtime = time.asctime(time.localtime(time.time()))

        protocol = packet.transport_layer
        src_addr = packet.ip.src
        dst_addr = packet.ip.dst

        # Create a unique connection key based on source and destination addresses
        connection_key = f"{src_addr} -> {dst_addr}"

        # Check if this connection attempt has not been printed yet
        if connection_key not in connection_attempts:
            print(f"User {src_addr} is trying to connect to {dst_addr} at {localtime}")
            connection_attempts[connection_key] = True

    except AttributeError as e:
        pass
    print("")