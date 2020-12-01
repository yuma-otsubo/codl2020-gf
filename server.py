#server.py

import sys
import time
from socket import *
BUFSIZE =5300 #一度に受信するデータサイズ
file_name =sys.arv[1]

def interact_with_client(s):
    start_time =time.time()
    req_msg =s.recv(BUFSIZE).decode()#最大BUFSIZEバイトを受信する
    send_size=int(req_msg.split()[0])#最初の空白文字までに書かれているのがサイズなのでそれを解釈する
    with open(file_name,'rb') as f:
	 data=f.read(send_size)
	 s.send(data)
    end_time=time.time()
    elapsed_time=end_time -start_time
    try:#GET
       #1で処理
       code="OK Sending" +file_name + "from" + x + "to" + y +"total"+ (y-x) + "bytes at" + elapsed_time +"\n"
       s.send(code.encode())
    except OSError:
        code="NG 101 No such file"
        s.send(code.encode())
	#print("NG 101 No such file")
    except NameError:
        code="NG 301 Invalid command"
        s.send(code.encode())
	#print("NG 301 Invalid command")
    except AttributeError:
        code="NG 102 Invalid range"
        s.send(code.encode())
	#print("NG 103 Invalid command")
    s.close()

a_number=44
readers_id=8
server_port = 50000 #+reades_id*100+a_number
server_socket = socket(AF_INET,SOCK_STREAM)#TCPを使う待ち受けようのソケット
server_socket.bind(('',server_port))#ポート番号をソケットに対応付ける
server_socket.listen(1)#クライアントからの接続を待つ
print('The server is ready to receive')

while True:
    #connection_s, addr = server_socket.accept()
    #sentence = connection_socket.recv(1024).decode()
    #connection_socket.send(sentence.encode())
    #connection_socket.close()
    s,addr =server_socket.accept()
    interact_with_client(s)#クライアントとの処理は別関数で

