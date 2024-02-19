import pygame
from Lib.gun import Gun
import Controls
def run():
    pygame.init()
    screen=pygame.display.set_mode((700,800))
    pygame.display.set_caption("Ranger")
    bg_color = (0,0,0)
    gun = Gun(screen)
    print()
    while True:
        Controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()
run()