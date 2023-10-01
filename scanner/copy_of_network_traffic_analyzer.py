import pyshark
import time

# Network interface to capture traffic from on your Windows machine (e.g., "Ethernet")
networkInterface = "Wi-Fi"

# IP address of your Kali Linux VM
kali_vm_ip = "192.168.1.206"  # Replace with your Kali VM's IP address

# Define your filter expression to capture traffic to/from your Kali VM
filter_expression = f"host {kali_vm_ip}"

capture = pyshark.LiveCapture(interface=networkInterface, bpf_filter="host 34.218.62.116" and "host 135.181.223.254")
print("Listening on %s" % networkInterface)

for packet in capture.sniff_continuously():
    try:
        localtime = time.asctime(time.localtime(time.time()))

        protocol = packet.transport_layer
        src_addr = packet.ip.src
        src_port = packet[protocol].srcport
        dst_addr = packet.ip.dst
        dst_port = packet[protocol].dstport

        print("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
    except AttributeError as e:
        pass
    print("")
