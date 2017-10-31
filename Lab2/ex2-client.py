import socket

s = socket.socket()
host = '127.0.0.1'
port = 12345
s.connect((host, port))

while True:
    cmd = input("> ")
    cmd.encode('utf-8')
    s.send(cmd)
    print(s.recv(1024))
