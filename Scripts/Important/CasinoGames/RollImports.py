import sys

sys.path.append("Scripts\\Important\\")
from imports import *



class PlayerComponent:
    def __init__(self , rect , money_given):
    
        self.rect = rect
        self.color =  (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.money_given = money_given
    def draw(self, surface):
        pygame.draw.rect(surface ,self.color  , self.rect)
        
    def roll_left(self):
        self.rect.x += 10
        if self.rect.x >= 800:
            self.rect.x = 0
        

        