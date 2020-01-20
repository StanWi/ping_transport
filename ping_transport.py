#!/usr/bin/python3
import os
from datetime import datetime

import yaml


def load_addresses(file: str) -> dict:
    """Return dict ip addresses from settings"""
    try:
        with open(file) as f:
            addresses = yaml.safe_load(f)
    except FileNotFoundError:
        addresses = {'addresses': {'127.0.0.1': 'localhost'}}
    return addresses['addresses']


def check_ping(address: str, name: str) -> None:
    """Check ping IP, if not, add IP to list"""
    response = os.system('timeout 1 ping -c 1 -i 1 ' + address + ' > /dev/null')
    if response != 0:
        print('{} ({}) is down!'.format(name, address))


if __name__ == '__main__':
    start_time = datetime.now()
    down_list = []
    file_addresses = 'transport_ip_list.yml'
    ip = load_addresses(file_addresses)
    for ip_address in ip.keys():
        check_ping(ip_address, ip[ip_address])
    print(datetime.now() - start_time)
