import socket
import threading
 
class Server:
    def __init__(self, port, host="localhost", maxClients=5, Handler=None, verbose=True):
        s = socket.socket()
        s.bind((host, port))
        s.listen(maxClients)
        self.ClientHandlers = []
        while True:
            c,addr = s.accept()
            if verbose:
                ip = str(addr[0]) + ":" + str(addr[1])
                print("[+] Connection from %s" % (ip))
            if Handler != None:
                t = threading.Thread(target=Handler, args=(c,addr))
                t.start()
                self.ClientHandlers.append(t)
           
def Receiver(clientsocket, address):
    while True:
        try:
            data = clientsocket.recv(16384)
            clientsocket.send(data)
        except:
            clientsocket.close()
            return
    clientsocket.close()
 
Server(6971, "localhost", 5, Receiver)
