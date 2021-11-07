# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script for port scanning


import socket
from IPy import IP


ipaddress = input('[+] Enter Target To Scan: ')


def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Port' + str(port) + ' Is Open')
    except:
        print('[-] Port' + str(port) + ' Is Closed')


converted_ip = check_ip(ipaddress)
for port in range(75,85):
    scan_port(ipaddress, port)