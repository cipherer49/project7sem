from scapy.all import *

from scapy.all import *

# Network interface to capture traffic from (replace with your interface name)
capture_interface = "eth0"

# Network interface to mirror captured traffic to (replace with your mirror interface)
mirror_interface = "Wi-Fi"

# Specific source IP address to capture traffic from
specific_source_ip = "192.168.1.202"  # Replace with the desired source IP address

# Filter expression to capture only IP traffic from the specific source IP
ip_filter = f"src {specific_source_ip}"

def capture_and_forward_packet(packet):
    # Forward the captured packet to the mirror interface
    sendp(packet, iface=mirror_interface, verbose=False)

try:
    print(f"Capturing traffic from {specific_source_ip} on {capture_interface} and mirroring to {mirror_interface}")

    # Start capturing packets on the capture interface with the specific source IP filter
    sniff(iface=capture_interface, prn=capture_and_forward_packet, filter=ip_filter, store=0)

except KeyboardInterrupt:
    print("Capture stopped.")
