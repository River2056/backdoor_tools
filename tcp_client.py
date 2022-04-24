import socket

TARGET_HOST = '192.168.1.103'
TARGET_PORT = 9998

def main():
    #create socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((TARGET_HOST, TARGET_PORT))

    # send some data
    client.send(b'GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n')

    # receive some data
    res = client.recv(4096)

    print(res.decode())
    client.close()

if __name__ == '__main__':
    main()
