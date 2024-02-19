import pygame,sys

def events(gun):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                     gun.mRight = True
                elif event.key == pygame.K_LEFT:
                     gun.mLeft = True     
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                     gun.mRight = False
                elif event.key == pygame.K_LEFT:
                     gun.mLeft = False     
