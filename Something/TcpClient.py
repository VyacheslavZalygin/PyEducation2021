import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 4321))
sock.send(bytes('not for man in the middle', 'utf-8'))
msg = sock.recv(65535)
print(msg)