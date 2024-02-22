import pygame,sys
from bullet import Bullet
def events(screen,gun,bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                     gun.mRight = True
                elif event.key == pygame.K_LEFT:
                     gun.mLeft = True     
                elif event.key == pygame.K_SPACE:
                     new_bullet = Bullet(screen,gun)
                     bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                     gun.mRight = False
                elif event.key == pygame.K_LEFT:
                     gun.mLeft = False   
                elif event.key == pygame.K_SPACE:
                     gun.mSpace = False         

def update(screen,bg_color,gun,bullets):
     screen.fill(bg_color)
     for bullet in bullets.sprites():
          bullet.draw_bullet()
     gun.output()
     pygame.display.flip() 
