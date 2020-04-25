import socket
import sys
import time
import hashlib

host = input("Host: ")
port = int(input("Port: "))
password = input("Password: ")
host_k = input("Host Key: ")
host_key = str(hashlib.sha256(str(str(host)+str(password)).encode('utf-8')).hexdigest())
if(host_k == host_key):
      s = socket.socket()
      s.connect((host, port))
      print("Connected to the server.")
      while 1:
            incoming_message = s.recv(1024)
            incoming_message = ((incoming_message.decode()).replace(host_key, ''))
            print("Server : ", incoming_message)
            print("------------------------------------")
            message = input(str(">> "))
            message = str(message+host_key).encode()
            s.send(message)
            print("Message has been sent.")
            print("Waiting for any incoming message...")
            print("-----------------------------------")
else:
      print("Host key is wrong.")