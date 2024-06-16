import sys
sys.path.append("Scripts\\Important\\")
import pygame
from credits_imena import *
pygame.init()
credits_font = pygame.font.SysFont('Consolas', 30)

credits_text_developer = credits_font.render(f"Developer : {developer}", True, (255, 255, 255))
credits_text_developer2 = credits_font.render(f"Developer : {developer2}", True, (255, 255, 255))
