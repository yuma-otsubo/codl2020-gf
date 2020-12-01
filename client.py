#SIZE
# GET （2つの書式とも）
# REP
import sys
from socket import *
server_port = int(sys.argv[1])
server_name = sys.argv[2]
client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect((server_name,server_port))

sentence = sys.argv[3]

client_socket.send(sentence.encode())
if sentence == "SIZE":
    received_ans = "size"
elif sentence == "GET":
    received_ans = "GET"
elif sentence == "REP":
    received_ans = "REP"

ans = client_socket.recv(1024)
print(ans.decode())
client_socket.close()