import pygame
import sys

sys.path.append("Scripts\\Important\\")
from imports import *




class ChatBox():
    def __init__(self, enabled  , rect , message ):
        self.enabled = enabled
        self.rect = rect
        self.message = message
        self.enableCooldown = 0.1
    def displayChat(self , surface):
        if self.enabled:
            pygame.draw.rect(surface, pygame.Color("white"), self.rect)
    def disableChat(self , event):
        if event.key == pygame.K_ESCAPE:
            self.enabled = False

    def writeMessage(self , event):
        if Chat.enabled:
            self.enableCooldown -= 1/30
            if self.enableCooldown <= 0:

                
                print(Chat.message)
                if event.key == pygame.K_BACKSPACE:
                    Chat.message = Chat.message[:-1]
                else:
                    Chat.message += chr(event.key)
    







Chat = ChatBox(False , pygame.Rect(0 , 431 , 300 , 169 ) , "")

