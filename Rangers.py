import pygame
from Lib.gun import Gun
from pygame.sprite import Group
import Controls

def run():
    pygame.init()
    screen=pygame.display.set_mode((700,800))
    pygame.display.set_caption("Ranger")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    while True:
        Controls.events(screen,gun,bullets)
        gun.update_gun()
        bullets.update()
        Controls.update(screen,bg_color,gun,bullets)
run()