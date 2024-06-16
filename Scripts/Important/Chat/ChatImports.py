import pygame
import sys

sys.path.append("Scripts\\Important\\")
from imports import *

pygame.init()
font = pygame.font.SysFont('Comic Sans MS' , 30)

class ChatBox():
    def __init__(self, enabled  , rect , message ):
        self.enabled = enabled
        self.rect = rect
        self.message = message
        self.enableCooldown = 0.2
    def displayChat(self , surface , cooldownrenderer , input_message_render):
        if self.enabled:
            self.enableCooldown -= 1/30
            pygame.draw.rect(surface, pygame.Color("white"), self.rect)
            if self.enableCooldown > 0:    
                self.renderMessageCooldown(surface , cooldownrenderer)
            self.renderMessageInput(surface , input_message_render)
            
    def disableChat(self , event):
        if event.key == pygame.K_ESCAPE:
            self.enabled = False
            self.message = ""
            self.enableCooldown = 0.2
            

    def writeMessage(self , event):
        if Chat.enabled:
            
            if self.enableCooldown <= 0:   
                print(Chat.message)
                if event.key == pygame.K_BACKSPACE:
                    Chat.message = Chat.message[:-1]
                    
                else:
                    Chat.message += chr(event.key)
    def renderMessageInput(self , screen , msgtorender):
        screen.blit(msgtorender , (0,560) )
    def renderMessageCooldown(self , screen , cooldowntorender):
        screen.blit(cooldowntorender , (69, 525))
                    
                    
    
                    
    







Chat = ChatBox(False , pygame.Rect(0 , 431 , 300 , 169 ) , "")

