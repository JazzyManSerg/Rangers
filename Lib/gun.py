import pygame

class Gun():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load('Resources/pixil-frame-0.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.mRight = False
        self.mLeft = False
    def output(self):
        self.screen.blit(self.image,self.rect)
    def update_gun(self):
        print(self.mLeft)
        if self.mRight and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.mLeft and self.rect.left>0 :
            self.rect.centerx -= 1
