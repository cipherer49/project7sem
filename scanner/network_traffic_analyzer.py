import pyshark
import time
networkInterface = "Wi-Fi"
capture = pyshark.LiveCapture(interface=networkInterface,bpf_filter =  "host 151.101.65.140" and "host 151.101.66.167")
print("Listening on %s" % networkInterface)
for packet in capture.sniff_continuously():
    try:
        localtime = time.asctime(time.localtime(time.time()))

        protocol = packet.transport_layer
        src_addr = packet.ip.src
        src_port = packet[protocol].srcport
        dst_addr = packet.ip.dst
        dst_port = packet[protocol].dstport

        #print("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
        print("user",src_addr,"is trying to connect to",dst_addr,"at",localtime)
    except AttributeError as e:
        pass
    print("")
