import pygame,sys
from bullet import Bullet
from ino import Ino
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

def update(screen,bg_color,gun,inos,bullets):
     screen.fill(bg_color)
     for bullet in bullets.sprites():
          bullet.draw_bullet()
     gun.output()
     inos.draw(screen)
     pygame.display.flip() 
     

def update_bullet(bullets):
     bullets.update()
     print(len(bullets))
     for bullet in bullets.copy():
          if bullet.rect.bottom<=0:
               bullets.remove(bullet)
def create_army(screen,inos): 
     ino=Ino(screen)
     ino_width=ino.rect.width
     number_ino_x=int((700-2*ino_width)/ino_width) 
     for ino_number in range(number_ino_x):
          ino=Ino(screen)
          ino.x=ino_width+ino_width*ino_number
          ino.rect=ino.x
          inos.add(ino)

