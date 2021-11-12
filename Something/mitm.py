#!/usr/bin/env python3
import socket
import threading

def extract_port(text):
  try:
    port = int(text)
    if port < 0 or port > 65535: return None
  except:
    return None
  return port

def is_ip(text):
  try:
    for oct in [int(x) for x in text.split('.')]:
      if oct < 0 or oct > 255:
        return False
    return True
  except:
    return False

def main():
  args = ['4321', '1234', '127.0.0.1']#sys.argv[1:]

  if len(args) == 0 or len(args) > 3:
    print("USAGE: ./mitm.py SRC_PORT DST_PORT DST_ADDRESS")
    return 1

  src_port = extract_port(args[0])
  if src_port == None:
    print("SRC_PORT must be in range 0 - 65535")
    return 2

  dst_port = extract_port(args[1])
  if dst_port == None:
    print("DST_PORT must be in range 0 - 65535")
    return 2

  dst_ip = args[2]
  if not is_ip(dst_ip):
    print("incorrect DST_ADDRESS")
    return 2

  server = socket.socket()
  server.bind(('', src_port))
  server.listen(0)
  print("SERVER ONLINE")

  client = socket.socket()
  client.connect((dst_ip, dst_port))
  print("CONNECTION WITH DIST HOST ESTABLISHED")

  while True:
    conn, addr = server.accept()
    print("CONNECTION ESTABLISHED WITH", addr)
    print("LISTENING")

    threading.Thread(target=from_src_to_dst, args=(conn, client)).start()
    threading.Thread(target=from_dst_to_src, args=(conn, client)).start()

    print("CONNECTION CLOSED WITH", addr)

def from_src_to_dst(conn, client):
  while True:
    data = conn.recv(65535)
    if len(data) == 0: break
    print('RECEIVED FROM SRC: ', data.decode('utf-8'))
    client.send(data)

def from_dst_to_src(conn, client):
  while True:
    data = client.recv(65535)
    if len(data) == 0: break
    print('RECEIVED FROM DST: ', data.decode('utf-8'))
    conn.send(data)

def to_hex(byte):  ## вместо этого обычно пользуются форматированием текстов
  ## например, "%02x" % byte
  text = hex(byte)[2:]
  if len(text) == 1: return '0' + text
  return text

def print_data(data):
  col = 0
  row = []
  for byte in data:
    print(to_hex(byte), end = ' ')
    col += 1
    row.append(byte)
    if col == 16:
      col = 0
      print(" | " + repr(str(bytes(row), 'utf-8'))[1:-1])
      row = []
  if col > 0:
    print(" | " + repr(str(bytes(row), 'utf-8'))[1:-1])
    # В качестве тривиального упражнения: перенести эту черту
    # в правильное место.
    #
    # В качестве нетривиального: если количество поступивших байт данных
    # не делится на количество колонок, отложить печать до поступления
    # новых данных (не удивляйтесь, если Вы не увидите частично
    # напечатанный текст: буфер печати опустошается обычно либо при
    # переходе на следующую строчку, либо при насильном его опустошении).

exit(main())

