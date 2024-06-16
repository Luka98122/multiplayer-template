import threading
import sys
import socket


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 14242

class Client():
    def __init__(self) -> None:
        self.name = 0
        self.id = 0
    def pr(self):
        print(f"Client: {self.name}, ID: {self.id}")
clients = []
client_socket = 0
def handle_server():
    global client_socket
    while True:
        try:
            data = client_socket.recv(1024)
        except Exception as e:
            if e.errno == 10054:
                print("Server disconnected")
                sys.exit()
                return
            print(f"Error: {e}")
        if data:
            dat = data.decode()
            if dat.startswith("<non>"): # Do not execute anything
                dat = dat.split("<non>")[1]
                if dat.startswith("<ac>"):
                    name = dat.split("<ac>")[1].split("|")[1]
                    msg = dat.split("<ac>")[1].split("|")[2]
                    print(f"[All Chat] {name}: {msg}")
            elif dat.startswith("<err>"):
                error1 = dat.split("<err>")[1]
                print(f"Error: {error1}")
            else: # Execute server commands
                if dat.startswith("<client>"):

                    new_client_name = dat.split("|")[1]
                    new_client_id = dat.split("|")[2]
                    cli = Client()
                    cli.name = new_client_name
                    cli.id = new_client_id
                    clients.append(cli)
                    print(f"Added client {cli.name}, ID: {cli.id}")
                if dat.startswith("<clientdc>"):
                    new_client_name = dat.split("|")[1]
                    new_client_id = dat.split("|")[2]
                    for i in range(len(clients)):
                        if clients[i].id == new_client_id:
                            print("Client Disconnected: ",end="")
                            clients[i].pr()
                            del clients[i]
                            break
                

def setup():
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
    except:
        print("Failed to connect to server. ( Server is offline )")
        exit()

    server_thread = threading.Thread(target=handle_server)
    server_thread.start()

    
    return [client_socket,server_thread]