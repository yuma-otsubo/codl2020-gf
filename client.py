#SIZE
# GET （2つの書式とも）
# REP
import sys
from socket import *
import pbl2
# server_port = int(sys.argv[1])
# server_name = sys.argv[2]
# client_socket = socket(AF_INET,SOCK_STREAM)
# client_socket.connect((server_name,server_port))

# sentence = sys.argv[3]

# client_socket.send(sentence.encode())
# if sentence == "SIZE":
#     received_ans = "size"
# elif sentence == "GET":
#     received_ans = "GET"
# elif sentence == "REP":
#     received_ans = "REP"

# ans = client_socket.recv(1024)
# print(ans.decode())

# def filesize(s):
#     pass
BUFSIZE = 4096
if  __name__ == "__main__":
    server_name = sys.argv[1]
    server_port = int(sys.argv[2])
    client_socket = socket(AF_INET,SOCK_STREAM)
    client_socket.connect((server_name,server_port))
    while True:
        com = input().split()
        if com[0] == "SIZE":
            mes = com[0] + com[1] + '\n'
            client_socket.send(mes.encode())
            with open(com[1],'wb') as f:
                while True:
                    data = client_socket.recv(BUFSIZE)
                    if len(data) <= 0:
                        break
                    f.write(data)
            client_socket.close()
        elif com[0] == "GET":
            part = com[3]
            getarg = pbl2.genkey(com[2])
            if part == "PARTIAL":
                a = com[4]
                b = com[5]
                mes = com[0] + com[1] + pbl2.genkey() + part + a + b + '\n'
                with open(com[1],'wb') as f:
                    while True:
                        data = client_socket.recv(BUFSIZE)
                        if len(data) <= 0:
                            break
                        f.write(data)
                client_socket.close()
                
            else:
                mes = com[0] + com[1] + pbl2.genkey() + part + '\n'
                with open(com[1],'wb') as f:
                    while True:
                        data = client_socket.recv(BUFSIZE)
                        if len(data) <= 0:
                            break
                        f.write(data)
                client_socket.close()
                client_socket.send(mes.encode())
        elif com[0] == "REP":
            pass
