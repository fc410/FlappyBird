import pygame
import functions
import variableDatabase

pygame.init()

# Sets the display screen with width and height respectively
# as a tuple
screen = pygame.display.set_mode((574, 800))
pygame.display.set_caption('FlappyBird')

# for frame work in the game
clock = pygame.time.Clock()

# font for the game
game_font = pygame.font.Font('04B_19.ttf', 40)

# Game variables


game_active = True


# importing the background image
back_ground_surface = pygame.image.load('assets/background-day.png').convert()

# resizing the background surface
back_ground_surface = pygame.transform.scale(back_ground_surface, (574, 800))

# importing the floor image
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0


game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(288, 350))



# Stores width of the screen into a variable
width = screen.get_width()

# Stores height of the screen into a variable
height = screen.get_height()



# Font type
font = pygame.font.SysFont(None, 30)

white = (255,255,255)


click = False
