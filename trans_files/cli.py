import socket  
import os
import time
from tqdm import tqdm
  
def send_file_to_server(filename, host, port):  
    # 创建客户端套接字  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    # 连接到服务端  
    client_socket.connect((host, port))  
    

    fileSize = os.path.getsize(filename)
    progress_bar = tqdm(total=fileSize, desc="Download File", ncols=100, ascii=True, bar_format="{l_bar}{bar}{r_bar}")

    # 打开文件  
    with open(filename, 'rb') as f:  
        # 逐块发送文件  
        while True:  
            data = f.read(10240)  # 每次读取10KB的数据  
            if not data:  
                break  
            client_socket.send(data )
            progress_bar.update(len(data))
        # 关闭客户端套接字  
        client_socket.close()

def send_file_size( filename, host, port):
    data = os.path.getsize(filename)

    filename = os.path.basename(filename)
    data = str(data) + "~" + filename

    data = data.encode(encoding= "utf-8")
    
    # 创建一个客户端套接字  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    
    # 连接到服务器  
    client_socket.connect((host, port))  
    
    # 发送数据到服务器  
    client_socket.sendall(data)  
    
    # 关闭套接字  
    client_socket.close()

if __name__ == "__main__":

    fileName = "VSCodeUserSetup-x64-1.82.2.zip"
    host = "175.27.191.84"
    port = 5000
    send_file_size( fileName, host, port)

    time.sleep(2)
    send_file_to_server( fileName, host, port)