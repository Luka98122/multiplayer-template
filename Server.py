import threading

import socket


class conn():
    def __init__(self) -> None:
        self.ip = 0
        self.port = 0
        self.connection = 0
        self.id = -1
        self.name = "noname"

available_ids = [1]*100

connections = []


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 14242

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_HOST, SERVER_PORT))


def handle_client(con):
    while True:
        try:
            data = con.connection.recv(1024)
        except Exception as e:
            if e.errno == 10054:
                available_ids[con.id] = 0
                print(f"{con.name} disconnected")
                
                
                for con2 in connections:
                    if con2!=con:
                        con2.connection.sendall(f"<clientdc>|{con.name}|{con.id}|".encode())
                for i in range(len(connections)):
                    if connections[i]==con:
                        del connections[i]
                        break
                return
            print(f"Error: {e}")
        if data:
            dat = data.decode().replace('\r','')
            print(f"[*] Received: {dat}")
            

            if dat.startswith("<set_name>") == True:
                print(f"CC: Name | {con.name} -> {dat.split('<set_name>')[1]}")
                con.name = dat.split("<set_name>")[1]
                for con2 in connections:
                    if con!=con2:
                        if con2.name!="noname":
                            con.connection.sendall(f"<client>|{con2.name}|{con2.id}|".encode())
                        if con.name!="noname":
                            con2.connection.sendall(f"<client>|{con.name}|{con.id}|".encode())

            if con.name=="noname":
                con.connection.sendall("Must set a name to send messages!".encode())
                continue

            if dat.startswith("<set_id>") == True:
                print(f"CC: ID | {con.id} -> {dat.split('<set_id>')[1]}")
                con.id = int(dat.split("<set_id>")[1])
            if dat.startswith("<ac>"):
                for con2 in connections:
                    if con2.id != con.id:
                        msg = "<non>"+"<ac>|"+con.name+"|"+dat.split("<ac>")[1]
                        print(msg)
                        con2.connection.sendall(msg.encode())
            
            


client_handlers = []

def get_new_connections():
    while True:
        server_socket.listen(5)
        print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

        client_socket, client_address = server_socket.accept()
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
        
        con1 = conn()
        con1.ip = client_address
        con1.connection = client_socket
        for i in range(len(available_ids)):
            if available_ids[i]==1:
                con1.id = i
                available_ids[i] = 0
                break
        
            
        connections.append(con1)
        t1 = threading.Thread(target=handle_client,args=[connections[-1]])
        t1.start()
        client_handlers.append(t1)

t = threading.Thread(target=get_new_connections)
t.start()
