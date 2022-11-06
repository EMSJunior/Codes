import pygame
from sys import exit

pygame.init()

displayw = 1200
displayh = 800
centerw = displayw/2
centerh = displayh/2
screenname = 'Invisible Mouse - byEhpsker'
screentick = 144

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

screen= pygame.display.set_mode((displayw, displayh))
pygame.display.set_caption(screenname)
clock = pygame.time.Clock()

test_surface =  pygame.Surface((100,100))
test_surface.fill('White')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface,(centerw - 50, centerh - 50))
            
    pygame.display.update()
    clock.tick(screentick)

