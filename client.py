import socket
import _thread

def client(client_name):
    client=socket.socket()
    client.connect(('localhost',9999))
    while True:
        msg="get current var_temp"
        client.send(msg.encode('utf-8'))
        data=client.recv(1024)
        if data.decode()=="over":
            client.close()
            break
        else:
            print(client_name," recv:",data.decode())
    client.close()

try:
   _thread.start_new_thread( client,("client-1",))
   _thread.start_new_thread( client,("client-2",))
   _thread.start_new_thread( client,("client-3",))
   _thread.start_new_thread( client,("client-4",))
except:
   print("Error: unable to start thread")

while 1:
   pass