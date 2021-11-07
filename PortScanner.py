# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script for port scanning


import socket
from IPy import IP


def scan(target, nr_of_ports):
    converted_ip = check_ip(target)     # Take the ip and store it in a variable
    print('\n' + '[Scanning target] ' + str(target))
    for port in range(1, int(nr_of_ports)):      # Scan ports for 1 to 100
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return (ip)     # If IP is a single ip return the value
    except ValueError:
        return socket.gethostbyname(ip)     # If a website is given the IP is returned by this function


def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)      # Set the timeout (accuracy depends on the timeout)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)       # For SW running on the open port
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass        # For closed ports


if __name__ == "__main__":      # This part is run only if PortScaner.py is run / not run if exported to other programs
    targets = input('Enter Target/s To Scan (Split Multiple Targets With ","): ')
    nr_of_ports = input('Enter The Number Of Ports you Want To Scan: ')
    if ',' in targets:      # For multiple targets delimitation
        for ip_add in targets.split(','):       # Scan each target sepparately if multiple
            scan(ip_add, nr_of_ports)
    else:
        scan(targets, nr_of_ports)       # Scan individual target