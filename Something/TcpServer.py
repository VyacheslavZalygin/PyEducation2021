import socket

sock = socket.socket()
sock.bind(('', 1234))

while True:
  sock.listen()
  print('Listening on 1234')
  conn, addr = sock.accept()
  print(f'Connection with {addr} established')

  while True:
    msg = conn.recv(65536)
    print(f'Received: {msg}')
    print(f'Address: {addr}')
    conn.sendto(b'hello', addr)

  print('disconnected')