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
    server_port = int(sys.argv[1])
    server_name = sys.argv[2]
    client_socket = socket(AF_INET,SOCK_STREAM)
    client_socket.connect((server_name,server_port))
    dem = sys.argv[3]
    fn = sys.argv[4]
    if dem == "SIZE":
        mes = dem + fn + '\n'
        client_socket.send(mes.encode())
        with open(fn,'wb') as f:
            while True:
                data = client_socket.recv(BUFSIZE)
                if len(data) <= 0:
                    break
                f.write(data)
        client_socket.close()
    elif dem == "GET":
        part = sys.argv[6]
        getarg = pbl2.genkey(sys.argv[5])
        if part == "PARTIAL":
            a = sys.argv[7]
            b = sys.argv[8]
            mes = dem + fn + pbl2.genkey() + part + a + b + '\n'
            with open(fn,'wb') as f:
                while True:
                    data = client_socket.recv(BUFSIZE)
                    if len(data) <= 0:
                        break
                    f.write(data)
            client_socket.close()
            
        else:
            mes = dem + fn + pbl2.genkey() + part + '\n'
            with open(fn,'wb') as f:
                while True:
                    data = client_socket.recv(BUFSIZE)
                    if len(data) <= 0:
                        break
                    f.write(data)
            client_socket.close()
            client_socket.send(mes.encode())
    elif dem == "REP":
        pass
