import pygame
import functions
import variableDatabase


def check_collision(pipes):
    for pip in pipes:
        if bird_rect.colliderect(pip):
            death_sound.play()
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 750:
        death_sound.play()
        return False

    return True


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect

pygame.init()

bird_movement = 0
gravity = 0.25

# importing the bird image
bird_down_flap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
bird_mid_flap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
bird_up_flap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_down_flap, bird_mid_flap, bird_up_flap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 400))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')

#importing bird images and resizing them
blueBird = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
redBird = pygame.transform.scale2x(pygame.image.load('assets/redbird-midflap.png').convert_alpha())
yellowBird = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha())