#!/usr/bin/python3

import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

file_name = 'transport_ip_list.txt'
addresses = []
down_list = []

def addresses_list(file_name):
    """Return list of list IP addresses and hostnames"""
    with open(file_name) as ip_list:
        for string in ip_list:
            if not string.startswith('#'):
                addresses.append(string.strip().split(';'))

def check_ping(ip: str, name: str) -> None:
    """Check ping IP, if not, add IP to list."""
    response = os.system('timeout 1 ping -c 1 -i 1 ' + ip + ' > /dev/null')
    if response != 0:
        down_list.append(name + ' (' + ip + ') is down!')

def  threads_conn(function, hostname, limit=2):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        pass


if __name__ == '__main__':
    start_time = datetime.now()
    addresses_list(file_name)
    for hostname in addresses:
        check_ping(hostname[0], hostname[1])
    for line in down_list:
        print(line)
    print(len(down_list))
    print(datetime.now() - start_time)
