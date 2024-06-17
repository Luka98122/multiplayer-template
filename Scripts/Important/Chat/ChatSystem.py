import pygame.draw

from ChatImports import *
import client


pygame.init()
pygame.font.init()
window = pygame.display.set_mode((800,600))
sat = pygame.time.Clock()
name = "deki"

client_socket,server_thread,clients,chat_stuff,other_stuff = client.setup()
client_socket.sendall(f"<set_name>{name}".encode())

prefixes = [["/ac ","<ac>"],["/dm ","<dm>"],["/name ","<set_name>"]]



renderovane_poruke = []
def renderMessages():

    renderovane_poruke.clear() 
    y_pos = 550
    for msg in reversed(chat_stuff[-7:]):  
        renderovane_poruke.append(MessageHolder(msg, (2, y_pos)))
        y_pos -= 20  

    for msg in renderovane_poruke:
        msg.rendermsg(window)
    
    
allChatToggle = False
dmChatToggle = False

def proverikomande():
    global prefixes
    for pre in prefixes:
        Chat.message = Chat.message.replace(pre[0],pre[1])
    client_socket.sendall(Chat.message.encode())
    Chat.message = ""


def chat():
    input_message_renderer = font.render(Chat.message , False , pygame.Color("white"))
    
    chatcooldown = f"{round(Chat.enableCooldown , 3)}"
    renderEnableCooldownText = font.render(chatcooldown  , False , pygame.Color("green"))
    
    last_seen = None
    running = True
    while running:
        
        if len(chat_stuff)!=0 and last_seen!=chat_stuff[-1]:
            last_seen = chat_stuff[-1]
            print(f"Just saw: {last_seen}")
            
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                client_socket.sendall('<disconnect>')
                running = False
                
                
            
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    Chat.enabled = True
                if event.key == pygame.K_RETURN:
                    if (Chat.enabled):
                        if Chat.message.strip() == "":
                            Chat.message = ""
                        elif Chat.message =='/chat a':
                            global allChatToggle
                            allChatToggle = not allChatToggle
                            chat_stuff.append('Toggled All Chat')       
                            Chat.message = ""
                        else:
                            if allChatToggle:
                                if Chat.message.startswith('/'):
                                    proverikomande()
                                    
                                else:
                                    client_socket.sendall(f"<ac>{Chat.message}".encode())
                                    Chat.message = ""
                            else:
                                proverikomande()

                        
                    
                        

                Chat.disableChat(event)
                if Chat.enabled:
                    
                    Chat.writeMessage(event)
                    Chat.message = Chat.message.replace('\r','')
                    input_message_renderer = font.render(Chat.message , False , pygame.Color("green"))
        window.fill((255,255,255))
        
        keys = pygame.key.get_pressed()
        Chat.displayChat(window , renderEnableCooldownText , input_message_renderer)
        
        if Chat.enableCooldown>0:   
            renderEnableCooldownText = font.render(chatcooldown , False , pygame.Color("green"))
            chatcooldown = f"{round(Chat.enableCooldown , 3)}"
        
        if Chat.enabled:
            renderMessages()

        

        pygame.display.flip()
        sat.tick(30)

    pygame.quit()
    
chat()



