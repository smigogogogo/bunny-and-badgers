import pygame
import math

class Bullet(pygame.sprite.Sprite):
    image=pygame.image.load('resources/images/bullet.png')
    def __init__(self,rabbit,screen,setting):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.angle = rabbit.angle
        self.image=pygame.transform.rotate(self.image,360 - self.angle * 57.29)
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = rabbit.rect.centerx, rabbit.rect.centery
        self.bullet_speed=setting.bullet_speed
    def update(self):
        velx=math.cos(self.angle)*self.bullet_speed
        vely=math.sin(self.angle)*self.bullet_speed
        self.rect.left += velx
        self.rect.top += vely

    def add_bullet(self):
            self.screen.blit(self.image, self.rect)
