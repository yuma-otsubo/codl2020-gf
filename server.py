#server.py

import sys
import time
import os
from socket import *
BUFSIZE =5300 #一度に受信するデータサイズ

def in_com(s):
    s.recv(1024).decode()
def interact_with_client(s,file_name):
    start_time =time.time()
    req_msg =s.recv(BUFSIZE).decode()#最大BUFSIZEバイトを受信する
    send_size=int(req_msg.split()[0])#最初の空白文字までに書かれているのがサイズなのでそれを解釈する
    words = in_com(s)
    # with open(file_name,'rb') as f:
    #      data=f.read(send_size)
    #      s.send(data)
    end_time=time.time()
    elapsed_time=end_time -start_time
    if words[0]=='GET':
    	try:#GET
       		file_name=words[1]
       		x=float(word[2])#pbl2.genkey()の結果を予め送る方法がわかんない
       		y=float(word[3])
       		code="OK Sending" +file_name + "from" + x + "to" + y +"total"+ (y-x+1) + "bytes at" + elapsed_time +"\n"
       		s.send(code.encode())
    	except FileNotFoundError:
        	code="NG 101 No such file"
        	s.send(code.encode())
    	except SyntaxError:#ここ自信ない
        	code="NG 301 Invalid command"
        	s.send(code.encode())
    	except KeyError:
        	code="NG 102 Invalid range"
        	s.send(code.encode())

    elif words[0]=='SIZE':
    	try:
       		words[1]=file_name
       		code="OK "+file_name+" "+os.path.getsize()+" bytes"
			with open(file_name,'rb') as f:
				data=f.read(send_size)
				s.send(data)
			print(code)
    	except FileNotFoundError:
        	code="NG 101 No such file"
        	s.send(code.encode())
    	except SyntaxError:#ここも同様
        	code="NG 301 Invalid command"
        	s.send(code.encode())

    elif words[0]=='REP':    
    	try:
       		words[1]=file_name
       		code="OK digest of "+file_name +" was successfully received REP at " +end_time
    	except FileNotFoundError:
        	code="NG 101 no such file"
        	s.send(code.encode())
    	except SyntaxError:
        	code="NG 301 Invalid command"
        	s.send(code.encode())
    	#except Error:
    	#時間の都合で途中

    
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
    file_name =sys.arv[1]
    s,addr =server_socket.accept()

    interact_with_client(s,file_name)#クライアントとの処理は別関数で

