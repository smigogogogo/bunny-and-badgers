import pygame


class End:
    def __init__(self,screen):
        self.screen=screen
        self.gameover=pygame.image.load('resources/images/gameover.png')
        self.gamewin=pygame.image.load('resources/images/youwin.png')
        self.end_image=None
    def final_loose(self):
        self.screen.blit(self.gameover,(0,0))

    def final_win(self):
        self.screen.blit(self.gamewin, (0, 0))

