import pygame
import random
import sys
from player import Player

from pygame.locals import *

TAMANHOTELA = (800,800)
BGColor = (255,255,255)
FPS = 60

pygame.init()
screen = pygame.display.set_mode(TAMANHOTELA)

# Run until the user asks to quit
player = Player()
running = True


clock = pygame.time.Clock()

pos = []

while running:

  # Did the user click the window close button?
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

  # Fill the background with white
  screen.fill(BGColor)

  # Draw a solid blue circle in the center
  player.draw(screen)
  print(player.rect)
  player.handle_keys()
  if((player.rect.x,player.rect.y) not in pos):
    pos.append((player.rect.x,player.rect.y))
  for i in pos:
    pygame.draw.rect(screen, (0, 0, 128),(i[0],i[1],16,16))
  # Flip the display
  pygame.display.flip()
  clock.tick(FPS)

# Done! Time to quit.
pygame.quit()