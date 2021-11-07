# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script for port scanning


import socket
from IPy import IP


targets = input('[Enter Target/s To Scan (split multiple targets with ","): ')


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[Scanning target] ' + str(target))
    for port in range(1, 100):
        scan_port(converted_ip, port)


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
        pass

if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add)
else:
    scan(targets)