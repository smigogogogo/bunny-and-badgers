import pygame
import sys

from bullet import Bullet
from badger import Badger


def check_events(rabbit,gamestat,bullet_group,screen,setting):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydownevents(event,rabbit)
        elif event.type==pygame.KEYUP:
            check_keyupevents(event,rabbit)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            gamestat.accuracy[1] += 1
            bullet=Bullet(rabbit,screen,setting)
            rabbit.shoot.play()
            bullet_group.add(bullet)


def check_keydownevents(event,rabbit):
    if event.key==pygame.K_w:
        rabbit.moveup=True
    elif event.key==pygame.K_a:
        rabbit.moveleft=True
    elif event.key==pygame.K_s:
        rabbit.movedown=True
    elif event.key==pygame.K_d:
        rabbit.moveright=True

def check_keyupevents(event,rabbit):
    if event.key==pygame.K_w:
        rabbit.moveup=False
    elif event.key==pygame.K_a:
        rabbit.moveleft=False
    elif event.key==pygame.K_s:
        rabbit.movedown=False
    elif event.key==pygame.K_d:
        rabbit.moveright=False


def check_end(gamestat, end):
    if pygame.time.get_ticks() >= 90000:
        gamestat.game_on = False
        end.end_image = True
    if gamestat.health_point <= 0:
        gamestat.game_on = False
        end.end_image = False


def show_ending(screen, exitcode, gamestat, end):
    font = pygame.font.Font(None, 24)
    gamestat.compute_accuracy()
    text = font.render(f"Accuracy: {gamestat.percentage}%", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    while True:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if exitcode:
            end.final_win()
        else:
            end.final_loose()
        screen.blit(text, text_rect)
        pygame.display.flip()
def check_generate_badger(gamestat, setting, badger_group, screen):
    if gamestat.badtimer == 0:
        badger = Badger(screen, setting)
        badger_group.add(badger)
        gamestat.badtimer = 100 - (setting.badger_generate_speed * 2)
        setting.badger_generate_speed = 20 if setting.badger_generate_speed >= 20 else setting.badger_generate_speed + 2
    gamestat.badtimer -= 1



def update_castle(setting, screen, castle):
    for y in range(25, (setting.screen_height - 30),
                   (castle.image.get_height()+5)):
        screen.blit(castle.image, (0, y))
def update_grass(setting, screen, grass):
    for x in range(setting.screen_width//grass.image.get_width()+1):
        for y in range(setting.screen_height//grass.image.get_height()+1):
            screen.blit(grass.image, (x*grass.image.get_width(),y*grass.image.get_height()))

def update_bullet(bullet_group,setting):
    for bullet in bullet_group:
        bullet.update()
        if bullet.rect.right<0 or bullet.rect.left>setting.screen_width or bullet.rect.top>setting.screen_height or bullet.rect.bottom<0:
            bullet_group.remove(bullet)
        bullet.add_bullet()

def update_badger(badger_group,bullet_group,gamestat):
    for badger in badger_group:
        badger.update()
        if badger.rect.left<64:
            badger_group.remove(badger)
            gamestat.health_point -=7
        for bullet in (bullet_group):
            if pygame.sprite.collide_mask(badger,bullet):
                badger_group.remove(badger)
                bullet_group.remove(bullet)
                gamestat.accuracy[0] += 1
        badger.add_badger()






def update_screen(setting,screen,rabbit,grass,castle,bullet_group,gamestat,badger_group,healthvalue, timebar,end):
    screen.fill(setting.bg_color)
    update_grass(setting, screen, grass)
    update_castle(setting, screen, castle)

    healthvalue.health_left(gamestat)
    timebar.update()
    timebar.drawtext()
    update_bullet(bullet_group, setting)
    update_badger(badger_group, bullet_group, gamestat)
    check_generate_badger(gamestat, setting, badger_group, screen)
    rabbit.update()
    rabbit.update_toward()
    rabbit.blitme()
    check_end(gamestat, end)
    if end.end_image is not None:
        show_ending(screen, end.end_image, gamestat, end)
    pygame.display.flip()