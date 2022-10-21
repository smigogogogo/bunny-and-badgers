import pygame
import function
from setting import Setting
from rabbit import Rabbit
from grass import Grass
from castle import Castle
from gamestat import Gamestat
from healthvalue import Healthvalue
from timebar import Timebar
from end import End


def run():

    pygame.init()
    pygame.mixer.init()
    setting=Setting()
    screen=pygame.display.set_mode((setting.screen_width,setting.screen_height))
    rabbit=Rabbit(screen)
    grass=Grass()
    castle=Castle()
    gamestat = Gamestat()
    bullet_group=pygame.sprite.Group()
    badger_group = pygame.sprite.Group()
    healthvalue = Healthvalue(screen)
    timebar = Timebar(screen)
    end=End(screen)
    pygame.display.set_caption("Bunnies and Badgers")
    pygame.mixer.music.load('resources/audios/moonlight.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)
    while gamestat.game_on:
        function.check_events(rabbit,gamestat,bullet_group,screen,setting)
        function.update_screen(setting,screen,rabbit,grass,castle,bullet_group,gamestat,badger_group,
                         healthvalue, timebar,end)
run()