import socket

ip = '10.0.0.209'
port = 110

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip,port))
s.recv(1024)

s.send('USER doink\r\n'.encode())
print(s.recv(1024).decode())

s.send('PASS theclown\r\n'.encode())
print(s.recv(1024).decode())

s.close()
