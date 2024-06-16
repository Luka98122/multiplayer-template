import pygame.draw

from ChatImports import *
import client


pygame.init()
window = pygame.display.set_mode((800,600))
sat = pygame.time.Clock()

client_socket = client.setup()
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
