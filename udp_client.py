import socket

TARGET_HOST = '192.168.1.102'
TARGET_PORT = 80

def main():
    # create a udp socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # send some data
    client.sendto(b'This is test data', (TARGET_HOST, TARGET_PORT))

    # receive some data
    data, addr = client.recvfrom(4096)

    print(data)
    print(addr)

if __name__ == '__main__':
    main()
