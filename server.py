import socketserver
 

HOST, PORT = "localhost", 9999
var_temp=int(input("输入var_temp:\n"))

class MyTCPHandler(socketserver.BaseRequestHandler): #每个客户端的请求过来，都会实例它。MyTCPHandler
    
    def handle(self): #重写handle()
        global var_temp
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                
                if self.data.decode()=="get current var_temp" and var_temp!=0:
                    var_temp-=1
                    self.request.sendall(str(var_temp).encode()) 
                else:
                    self.request.sendall("over".encode())
            except ConnectionResetError as e:
                print('Error is: ',e) #客户端断开时抛出的异常
                break
 

print("开始监听.......")
server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()