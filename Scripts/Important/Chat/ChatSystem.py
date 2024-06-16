import pygame.draw

from ChatImports import *



pygame.init()
window = pygame.display.set_mode((800,600))
sat = pygame.time.Clock()


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

def handle_server():
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

                    


try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
except:
    print("Failed to connect to server. ( Server is offline )")
    exit()

server_thread = threading.Thread(target=handle_server)
server_thread.start()

client_socket.sendall("<set_name>DekiNPC".encode())

def chat():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    Chat.enabled = True
                if event.key == pygame.K_RETURN:
                    client_socket.sendall(f"<ac>{Chat.message}".encode())

                Chat.disableChat(event)
                if Chat.enabled:
                    Chat.writeMessage(event)


        window.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        Chat.displayChat(window)







        pygame.display.flip()
        sat.tick(30)

    pygame.quit()
chat()

"""


            elif event.type == pygame.MOUSEBUTTONDOWN:
                choose_name_input_active = True
                player_name = ""
            elif event.type == pygame.KEYDOWN and choose_name_input_active:
                if event.key == pygame.K_RETURN:
                    choose_name_input_active = False

                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode
        prozor.fill((pygame.Color("black")))
        prozor.blit(choose_name_title, (100, 70))
        text_surf = choose_name_font.render(player_name, True, (255, 255, 255))
        prozor.blit(text_surf, text_surf.get_rect(center=prozor.get_rect().center))
        global trenutno_stanje
        trenutno_stanje = GameStates.CHOOSE_NAME
        with open("Saves/trenutno_stanje.pickle", "wb") as f:
            pickle.dump(trenutno_stanje, f)

        sat.tick(30)
        pygame.display.flip()
"""
