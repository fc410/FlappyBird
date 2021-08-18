import pygame
import random
import functions
import variableDatabase
import images
from variableDatabase import db, cursor


pygame.init()


def score_display(game_state):
    if game_state == 'mainGame':
        score_surface = images.game_font.render(('Score: ' + str(int(score))), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 50))
        images.screen.blit(score_surface, score_rect)
    if game_state == 'gameOver':
        score_surface = images.game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 50))
        images.screen.blit(score_surface, score_rect)

        high_score_surface = images.game_font.render(('High Score: ' + str(int(high_score))), True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(288, 650))
        images.screen.blit(high_score_surface, high_score_rect)

    if game_state == 'mainMenu':
        functions.main_menu()


def update_score(s, hs):
    if s > hs:
        hs = s
        cursor.execute("UPDATE HighScore SET highscore={} WHERE place=1".format(score))
        db.commit()
    return hs


def scoring(s, pipes):
    for pip in pipes:
        if pip.centerx <= 400:
            s += 1

cursor.execute("SELECT * FROM HighScore")

high_score_list = []

for x in cursor:
    high_score_list.append(x)

score = 0
high_score = high_score_list[0][1]

score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 150
