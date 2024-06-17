import pygame
import sys

sys.path.append("Scripts\\Important\\")
from imports import *

pygame.init()
font = pygame.font.SysFont('Comic Sans MS' , 14)
TextBox = pygame.image.load("Pictures\TextBox\TextBox.png")
TextBox.set_alpha(70)
InputTextBox = pygame.image.load("Pictures\TextBox\InputTextBox.png")

class ChatBox():
    def __init__(self, enabled  , rect , message ):
        self.enabled = enabled
        self.rect = rect
        self.message = message
        self.enableCooldown = 0.2
    
    def displayChat(self , surface , cooldownrenderer , input_message_render):
        if self.enabled:
            self.enableCooldown -= 1/30
            #pygame.draw.rect(surface, pygame.Color("white"), self.rect)
            surface.blit(TextBox ,(0 , 430) )
            
            if self.enableCooldown > 0:    
                self.renderMessageCooldown(surface , cooldownrenderer)
            else:
                surface.blit(InputTextBox , (0 , 574))
            self.renderMessageInput(surface , input_message_render)
            
    def disableChat(self , event):
        if event.key == pygame.K_ESCAPE:
            self.enabled = False
            self.message = ""
            self.enableCooldown = 0.2
            

    def writeMessage(self, event):
        if self.enabled:

            if self.enableCooldown <= 0:
                print(Chat.message)
                if event.key == pygame.K_BACKSPACE:
                    Chat.message = Chat.message[:-1]
                else:
                    keys_pressed = pygame.key.get_pressed()
                    if keys_pressed[pygame.K_LSHIFT] or keys_pressed[pygame.K_RSHIFT]:
                        if event.unicode.isalpha():
                            Chat.message += event.unicode.upper()
                        else:
                            Chat.message += event.unicode
                    else:
                        Chat.message += event.unicode
                    if(len(Chat.message) > 25):
                        Chat.message = Chat.message[:-1]          
                        print("Reached Limit!")
                    

    def renderMessageInput(self , screen , msgtorender):
        screen.blit(msgtorender , (4,570) )
    def renderMessageCooldown(self , screen , cooldowntorender):
        screen.blit(cooldowntorender , (69, 525))
                    
                    
    
                    
class MessageHolder():
    def __init__(self , messagecontent , position):
        self.messagecontent = messagecontent
        self.position = position
    def rendermsg(self , surface):
        surface.blit(font.render(self.messagecontent , False , pygame.Color("green")) , self.position)
        







Chat = ChatBox(False , pygame.Rect(0 , 431 , 300 , 169 ) , "" )

