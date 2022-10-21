import pygame
import random
class Badger(pygame.sprite.Sprite):
    image=pygame.image.load('resources/images/badguy.png')
    def __init__(self,screen,setting):
        pygame.sprite.Sprite.__init__(self)
        self.damage = pygame.mixer.Sound("resources/audios/explode.wav")
        self.hit = pygame.mixer.Sound("resources/audios/enemy.wav")
        self.damage.set_volume(0.05)
        self.hit.set_volume(0.05)
        self.screen=screen
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left=setting.screen_width
        self.rect.top=random.randint(30,setting.screen_height-30)
        self.badger_speed = setting.badger_speed
    def update(self):
        self.rect.left-=self.badger_speed
    def add_badger(self):
        self.screen.blit(self.image,self.rect)