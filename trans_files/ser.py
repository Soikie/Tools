import socket  
from tqdm import tqdm
  
def receive_file_from_client(host, port,total_size,fileName):  
    # 创建服务端套接字  
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    # 监听端口  
    server_socket.bind((host, port))  
    server_socket.listen(1)  
    print('等待客户端连接...')  
    # 接受客户端连接请求并进行通信  
    client_socket, addr = server_socket.accept()  
    print(f'客户端地址: {addr}')  
    print('开始接收文件...')  
    progress = 0  
    progress_bar = tqdm(total=total_size, desc="Download File", ncols=100, ascii=True, bar_format="{l_bar}{bar}{r_bar}")
    while True:  
        data = client_socket.recv(10240)  # 每次接收10KB的数据  
        if not data:  
            break  
        with open(fileName, 'ab') as f:  # 注意，这里我们打开文件用于追加（ab）模式，因为我们是从网络接收的数据流。  
            f.write(data)  # 将数据写入文件。这里可以修改数据的大小，比如1KB，取决于你的需求。  
        progress += len(data)  # 更新进度。注意，这里我们使用len(data)，因为我们是将原始数据写入文件，而不是读取的字节数。你可能需要修改这个以适应你的需求。
        progress_bar.update(len(data)) 
    print('文件接收完成！')  # 当没有更多数据可接收时，打印此消息。  
    client_socket.close()  # 关闭客户端套接字。注意，服务器不需要关闭其套接字，因为它们通常保持打开状态，直到程序结束。但是你可能想在这里关闭它以防止内存泄漏。你可能需要修改这个以适应你的需求。


def receive_file_size(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    
    # 绑定到本地地址和端口号  
    server_socket.bind((host, port))  
    
    # 监听连接请求  
    server_socket.listen(1)  
    print('等待客户端连接...')  
    
    # 接受连接请求并接收数据  
    client_socket, addr = server_socket.accept()  
    print(f'客户端地址: {addr}')  
    print('接收数据...')  
    data = client_socket.recv(1024)  
    data = data.decode("utf-8")

    data = data.split("~")
    fileSize,fileName = data

    print(f"文件大小为{fileSize}")
    print(f"文件名字为{fileName}")
    # 关闭套接字  
    client_socket.close()
    return fileSize,fileName

if __name__ == "__main__":

    host = "127.0.0.1"
    port = 5000
    fileSize,fileName = receive_file_size(host,port)
    fileSize = int(fileSize)
    receive_file_from_client(host,port,fileSize,fileName)
