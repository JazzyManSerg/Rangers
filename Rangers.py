import sys
import pygame
from Lib.gun import Gun
def run():
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Ranger")
    bg_color = (0,0,0)
    gun = Gun(screen)
    print()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()
run()