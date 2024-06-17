import sys

from RollImports import *



pygame.init()
screen = pygame.display.set_mode((800,600))
sat = pygame.time.Clock()

background = pygame.image.load("Pictures\\RollGame\\rollbg.png")
playerchooser_bg = pygame.image.load("Pictures\\RollGame\\playerchooserbg.png")
playerchooser_bg = pygame.transform.scale(screen , (800 , 110))
playerchooser_bg.set_alpha(128)



player_list = [PlayerComponent(pygame.Rect(0 , 130 , 100 , 110)  , 10)

               ]
    
                


def OnPlayerJoin():
    
        
    player_list.append(PlayerComponent(pygame.Rect(player_list[-1].rect.x + player_list[-1].rect.width , 130 ,  110 , 110 ),100))
    suma = 0
    for player in player_list:
        suma += player.money_given 
    for player in player_list:
        player.rect.width = 800 * (player.money_given / suma)

OnPlayerJoin()
def roll():
    working = True
    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False

        screen.fill((0,0,0))
        screen.blit(background , (0,0))
        screen.blit(playerchooser_bg , (0 , 130))

        
        for player in player_list:
            player.draw(screen)
            player.roll_left()
        
        
        pygame.display.flip()
        sat.tick(30)
    pygame.quit()
roll()