import sqlite3
import socket



def fetch_dns_data_from_database():
    conn = sqlite3.connect('D:\panapticon\dns_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT column1,column2 FROM ip_data')
    dns_data = cursor.fetchall()
    conn.close()
    return dns_data



def dns_to_ip():
    dns_data = fetch_dns_data_from_database()  # Fetch DNS data from the database

    for dns_name_tuple in dns_data:
        column1, dns_name = dns_name_tuple  # Unpack the tuple into column1 and dns_name
        try:
            ip_address = socket.gethostbyname(dns_name)
            print(f"Id: {column1}, DNS Name: {dns_name}, IP Address: {ip_address}")
        except socket.gaierror as e:
            print(f"Id: {column1}, DNS Name: {dns_name}, Error: {e}")

if __name__ == "__main__":
    dns_to_ip()