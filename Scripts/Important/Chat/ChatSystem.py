import pygame.draw

from ChatImports import *
import client


pygame.init()
pygame.font.init()
window = pygame.display.set_mode((800,600))
sat = pygame.time.Clock()


client_socket,server_thread = client.setup()
client_socket.sendall("<set_name>DekiNPC".encode())




message_to_render = font.render(Chat.message , False , pygame.Color("white"))



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
                    Chat.message = "" # pravi bug !!!

                Chat.disableChat(event)
                if Chat.enabled:
                    Chat.writeMessage(event)
                    message_to_render = font.render(Chat.message , False , pygame.Color("white"))


        window.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        Chat.displayChat(window)







        pygame.display.flip()
        sat.tick(30)

    pygame.quit()
chat()

