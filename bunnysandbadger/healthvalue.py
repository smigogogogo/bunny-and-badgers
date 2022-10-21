import pygame

class Healthvalue():
    def __init__(self,screen):
        self.image=pygame.image.load('resources/images/healthbar.png')
        self.image_cover=pygame.image.load('resources/images/health.png')
        self.screen=screen
    def health_left(self,gamestat):
        self.screen.blit(self.image, (5, 5))
        for i in range(gamestat.health_point):
            self.screen.blit(self.image_cover, (i + 8, 8))