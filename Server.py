import threading

import socket


class conn():
    def __init__(self) -> None:
        self.ip = 0
        self.port = 0
        self.connection = 0
        self.id = -1
        self.name = "noname"
        self.thread = 0
        self.index = 0

available_ids = [1]*100

kicked = []

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
        for i in range(len(kicked)):
            if con.name == kicked[i]:
                del kicked[i]
                return
        if data:
            dat = data.decode().replace('\r','')
            print(f"[*] Received: {dat}")
            if dat ==  "<diconnect>":
                for con2 in connections:
                    if con2!=con:
                        con2.connection.sendall(f"<clientdc>|{con.name}|{con.id}|".encode())
                con.connection.sendall("ByeBye".encode())
                for i in range(len(connections)):
                    if connections[i]==con:
                        del connections[i]
                        break           

            if dat.startswith("<set_name>") == True:
                name = dat.split("<set_name>")[1]
                name = name.rstrip()
                if name.count(" ")>0:
                    con.connection.sendall("<err> Name contains a space!".encode())
                    continue
                
                
                do_break = False
                for con2 in connections:
                    if con2.name == dat.split("<set_name>")[1]:
                        con.connection.sendall("<err> Name already taken!".encode())
                        do_break = True
                        break
                if do_break:
                    continue
                
                print(f"CC: Name | {con.name} -> {dat.split('<set_name>')[1]}")
                if con.name!="noname":
                    for con2 in connections:
                        con2.connection.sendall(f"<client_rename>|{con.name}|{dat.split('<set_name>')[1]}".encode())
                    con.name = dat.split("<set_name>")[1]
                    continue
                else:
                    con.name = dat.split("<set_name>")[1]
                for con2 in connections:
                    if con2.name!="noname":
                        con.connection.sendall(f"<client>|{con2.name}|{con2.id}|".encode())
                    if con.name!="noname":
                        con2.connection.sendall(f"<client>|{con.name}|{con.id}|".encode())

            if con.name=="noname":
                con.connection.sendall("Must set a name to send messages!".encode())
                continue

            if dat.startswith("<ac>"):
                for con2 in connections:
                    msg = "<non>"+"<ac>|"+con.name+"|"+dat.split("<ac>")[1]
                    print(msg)
                    con2.connection.sendall(msg.encode())
            if dat.startswith("<dm>"):
                name1 = dat.split("<dm>")[1].split(" ")[0]
                text = dat.split("<dm>")[1].replace(name1,"")
                for con2 in connections:
                    if con2.name ==name1:
                        con2.connection.sendall(f"<non><dm>|{con.name}|{text}".encode())
                
            


client_handlers = []

def get_new_connections():
    cnt = 0
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
        
        con1.index = cnt
        connections.append(con1)
        t1 = threading.Thread(target=handle_client,args=[connections[-1]])
        t1.start()
        connections[-1].thread = t1
        client_handlers.append(t1)
        cnt+=1
        

t = threading.Thread(target=get_new_connections)
t.start()

while True:
    command = input()
    if command.startswith("/kick"):
        name_or_id = command.split(" ")[1]
        for i in range(len(connections)):
            if name_or_id == connections[i].name or name_or_id == str(connections[i].id):
                for con2 in connections:
                    if con2!=connections[i]:
                        con2.connection.sendall(f"<clientdc>|{connections[i].name}|{connections[i].id}|".encode())
                connections[i].connection.sendall("ByeBye".encode())
                kicked.append(connections[i].name)
                del client_handlers[connections[i].index]
                del connections[i].thread
                del connections[i]
                break
                
            
    if command.startswith("/rename"):
        new_name = command.split(" ")[2]
        name = command.split(" ")[1]
        name = name.rstrip()

        
        
        do_break = False
        for con2 in connections:
            if con2.name == new_name:
                print("<err> Name already taken!")
                do_break = True
                break
        if do_break:
            continue
        
        print(f"CC: Name | {name} -> {new_name}")
        for con2 in connections:
            if con2.name == name:
                pass
            else:
                con2.connection.sendall(f"<client_rename>|{name}|{new_name}".encode())
        for con3 in connections:
            if con3.name == name:
                con3.name = new_name
                break
        continue
        pass
    