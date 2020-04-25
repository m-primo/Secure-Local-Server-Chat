import socket
import hashlib
import random
import uuid
s = socket.socket()
host_name = socket.gethostname()
password = str(str(int(random.random()*300000))+str(uuid.uuid4()))
host_key = str(hashlib.sha256(str(str(host_name)+str(password)).encode('utf-8')).hexdigest())