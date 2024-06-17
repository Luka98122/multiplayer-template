import threading
import sys
import socket
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 14242

chat_stuff = []
other_stuff = []





class Client():
    def __init__(self) -> None:
        self.name = 0
        self.id = 0
        self.money = 0
        self.perms = 0
    def pr(self):
        print(f"Client: {self.name}, ID: {self.id}")

def dict_to_client_obj(d :dict):
    cli = Client()
    cli.name = d["name"]
    cli.id = d["id"]
    cli.money = d["money"]
    cli.perms = d["perms"]
    return cli


clients = []
client_socket = 0
def handle_server():
    global client_socket
    global other_stuff
    global chat_stuff
    global clients
    while True:
        try:
            data = client_socket.recv(1024)
        except Exception as e:
            if e.errno == 10054:
                print("Server disconnected")
                other_stuff.append("Server disconnected")
                sys.exit()
                return
            print(f"Error: {e}")
        if data:
            dat = data.decode()
            if dat == "ByeBye":
                print("Server disconnected")
                sys.exit()
                return
            if dat.startswith("<non>"): # Do not execute anything
                dat = dat.split("<non>")[1]
                if dat.startswith("<ac>"):
                    name = dat.split("<ac>")[1].split("|")[1]
                    msg = dat.split("<ac>")[1].split("|")[2]
                    print(f"[All Chat] {name}: {msg}")
                    chat_stuff.append(f"[All Chat] {name}: {msg}")
                if dat.startswith("<dm>"):
                    name = dat.split("<dm>")[1].split("|")[1]
                    msg = dat.split("<dm>")[1].split("|")[2]
                    print(f"{name} -> You: {msg}")
                    chat_stuff.append(f"{name} -> You: {msg}")
            elif dat.startswith("<err>"):
                error1 = dat.split("<err>")[1]
                print(f"Error: {error1}")
                other_stuff.append(f"Error: {error1}")
            else: # Execute server commands
                if dat.startswith("<clients_update>"):
                    
                    clients.clear()
                    #clients = []
                    main_obj = dat.split("<clients_update>")[1]
                    main_obj = json.loads(main_obj)

                    for item in main_obj:
                        item = dict_to_client_obj(json.loads(item))
                        clients.append(item)
            
                    
                

def setup():
    global client_socket
    global chat_stuff
    global other_stuff
    global clients
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
    except:
        print("Failed to connect to server. ( Server is offline )")
        exit()

    server_thread = threading.Thread(target=handle_server)
    server_thread.start()

    
    return [client_socket,server_thread,clients,chat_stuff,other_stuff]