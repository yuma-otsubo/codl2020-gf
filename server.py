#server.py

import sys
import time
import os
from socket import *
BUFSIZE =5300 #一度に受信するデータサイズ
file_name ='random_1M.dat'#読み書きするファイルサイズ

##
#ファイル分割するやつ
def divide_file(filePath,chunkSize):
    readedDAtaSize=0
    i=0
    fileList=[]
    f=open(filePath,"rb")
    contentLength=os.path.getsize(filePath)#読み終わるまで繰り返す
    while readedDataSize<contentLEngth:
          f.seek(readedDataSize)#読み取り位置をシーク
          data=f.read(chunkSize)#指定したサイズだけ読み込む
          saveFilePath=filePath+"."+str(i)#分割ファイル保存
          with open(saveFilePath,'wb')as saveFile:
              saveFile.write(data)
          readedDataSize=readedDataSize+len(data)#読み込んだデータサイズの更新
          i=i+1
          fileList.append(saveFilePath)
    return fileList

##
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
       sentence=s.recv(1024).decode()
       x=10 #GETのXXXX
       y=int(sentence)#GETのYYYY
       z=y-x+
        #1で処理
       code="OK Sending" +name + "from" + x + "to" + y +"total"+ z + "bytes at" + elapsed_time +"\n"
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

