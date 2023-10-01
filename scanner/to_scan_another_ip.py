import socket

# Function to perform a TCP port scan on a target IP address
def tcp_port_scan(target_ip, port_range):
    open_ports = []

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((target_ip, port))
            open_ports.append(port)
            sock.close()
        except (socket.timeout, ConnectionRefusedError):
            pass

    return open_ports

def main():
    target_ip = input("Enter the target IP address: ")
    port_range = range(1, 100)  # Example: Scan ports from 1 to 1024

    open_ports = tcp_port_scan(target_ip, port_range)

    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip}")

if __name__ == "__main__":
    main()