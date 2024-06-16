import pygame
import sys

sys.path.append("Scripts\\Important\\")
from imports import *

pygame.init()
font = pygame.font.SysFont('Comic Sans MS' , 22)
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
            

    def writeMessage(self , event):
        if Chat.enabled:
            
            if self.enableCooldown <= 0:   
                print(Chat.message)
                if event.key == pygame.K_BACKSPACE:
                    Chat.message = Chat.message[:-1]
                    
                else:
                
                    if(len(Chat.message) < 25):
                        self.reachedMessageLimit = False
                        Chat.message += chr(event.key)
                    elif(len(Chat.message) > 25):
                        Chat.message = Chat.message[:-1]          
                        print("Reached Limit!")
                    else:
                        Chat.message += chr(event.key)
                        if len(Chat.message) == 25:
                            self.reachedMessageLimit = True

    def renderMessageInput(self , screen , msgtorender):
        screen.blit(msgtorender , (4,570) )
    def renderMessageCooldown(self , screen , cooldowntorender):
        screen.blit(cooldowntorender , (69, 525))
                    
                    
    
                    
    







Chat = ChatBox(False , pygame.Rect(0 , 431 , 300 , 169 ) , "" )

