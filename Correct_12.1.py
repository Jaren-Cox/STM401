import socket

url = input('Enter a URL: ')
sock = url.split("/")
port = sock[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((port, 80))

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data)

mysock.close()
