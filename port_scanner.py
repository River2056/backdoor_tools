#!/usr/local/bin/python3

import sys
import socket
import argparse
import textwrap
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from datetime import datetime

def handle(target, port):
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.setdefaulttimeout(1)
    # result = s.connect_ex((target, port))
    # if result == 0:
    #     print(f'Port {port} is open')
    # s.close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f'Port {port} is open')

def main():
    parser = argparse.ArgumentParser(
        description='Port scanner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            ./port_scanner.py -t 10.155.137.31 -s 1 -e 1000
        ''')
    )
    parser.add_argument('-t', '--target', help='specified IP address')
    parser.add_argument('-s', '--start', type=int, default=1, help='starting range of port')
    parser.add_argument('-e', '--end', type=int, default=1000, help='ending range of port')
    args = parser.parse_args()

    ip = args.target
    port_start = args.start
    port_end = args.end

    if not ip:
        print('Please provide ip address!')
        print('use -h for help')
        sys.exit(1)

    target = socket.gethostbyname(ip)

    print('-' * 60)
    print(f'Scanning target {target}')
    print(f'Time started {datetime.now()}')
    print('-' * 60)

    try:
        with ThreadPoolExecutor() as executor:
            results = [executor.submit(handle, target, port) for port in range(port_start, port_end+1)]

    except KeyboardInterrupt:
        print('Program terminated.')
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved')
        sys.exit(1)

    except socket.error:
        print('Couldn\'t connect to server')
        sys.exit()

if __name__ == '__main__':
    main()
