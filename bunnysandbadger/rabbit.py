import pygame
import math

class Rabbit:
    def __init__(self,screen):
        self.shoot = pygame.mixer.Sound("resources/audios/shoot.wav")
        self.image = pygame.image.load('resources/images/dude.png')
        self.shoot.set_volume(0.05)
        self.screen=screen
        self.moveup=False
        self.moveleft=False
        self.movedown=False
        self.moveright=False
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rotateimg = self.image
        self.roteterect = self.rect
        self.angle=0




    def update(self):
        if self.moveup:
            self.rect.centery-=3
        if self.moveleft:
            self.rect.centerx -= 3
        if self.movedown:
            self.rect.centery += 3
        if self.moveright:
            self.rect.centerx += 3
    def update_toward(self):
        position = pygame.mouse.get_pos()
        self.angle = math.atan2(position[1] - self.rect.centery + 32,
                                position[0] - self.rect.centerx + 26)
        self.rotateimg = pygame.transform.rotate(self.image, 360-self.angle*57.29)
        self.roteterect = (self.rect.centerx - self.rotateimg.get_rect().width/2,
                           self.rect.centery - self.rotateimg.get_rect().height/2)

    def blitme(self):
        self.screen.blit(self.rotateimg, self.roteterect)
