import socket


def dns_to_ip(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        return f"Error: {e}"


def main():
    domain_name = input("Enter a domain name: ")
    ip_address = dns_to_ip(domain_name)

    if ip_address:
        print(f"IP Address for {domain_name}: {ip_address}")
    else:
        print(f"Failed to resolve IP address for {domain_name}")


if __name__ == "__main__":
    main()