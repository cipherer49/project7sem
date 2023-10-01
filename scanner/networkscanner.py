import pyshark
option = input("choose a / b:")
try:
    if option == 'a':
        option = 'Wi-Fi'
    elif option == 'b':
        option = 'eth0'
except:
    print("Invalid option")



capture = pyshark.LiveCapture(interface = option)
for packet in capture.sniff_continuously(packet_count=10):
    print(packet)
