import socket
import sys
import time
import config

host_key = config.host_key
host = config.host_name
password = config.password
s = config.s
print("Host:", host)
port = int(input("Port: "))
print("Port:", port)
print("Password:", password)
print("Host Key:", host_key)
s.bind((host, port))
print("Server done binding to host and port successfully.")
print("Server is waiting for incoming connections...")
s.listen(1)
conn, addr = s.accept()
print(addr, "New connection to the server.")
print("")
while 1:
      message = input(str(">> "))
      message = str(message+host_key).encode()
      conn.send(message)
      print("Message has been sent.")
      print("Waiting for any incoming message...")
      print("-----------------------------------")
      incoming_message = conn.recv(1024)
      incoming_message = ((incoming_message.decode()).replace(host_key, ''))
      print("Client : ", incoming_message)
      print("-----------------------------------")
