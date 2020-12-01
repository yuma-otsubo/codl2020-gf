from socket import *

server_port = 50000
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print('The server is ready to receive')

while True:
    connection_socket , addr = server_socket.accept()
    sentence = connection_socket.recv(1024).decode()


    connection_socket.send(sentence.encode())
    connection_socket.close()