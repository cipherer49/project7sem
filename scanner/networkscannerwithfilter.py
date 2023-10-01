#collecting tcp packages only
import pyshark
capture = pyshark.LiveCapture(interface = 'Wi-Fi',bpf_filter = 'tcp port 80')
capture.sniff(packet_count = 5)
print(capture)
for packet in capture:
    print(packet.highest_layer)