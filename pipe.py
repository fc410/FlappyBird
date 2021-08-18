import pygame
import random
import functions
import variableDatabase
import images

pygame.init()


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 250))
    return bottom_pipe, top_pipe


def move_pipes(pipes, s):
    for pip in pipes:
        pip.centerx -= 5
        if pip.centerx <= 400:
            s += 1
    return pipes


def draw_pipes(pipes):
    for pip in pipes:
        if pip.bottom >= 800:
            images.screen.blit(pipe_surface, pip)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            images.screen.blit(flip_pipe, pip)


# importing pipe images
pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [300, 400, 600]
