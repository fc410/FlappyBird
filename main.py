import pygame
import sys
from bird import Bird
from pipe import Pipe
from screen import UIScreen
from buttons import Button
from database import cursor, db

pygame.init()

# For frame work in the game
clock = pygame.time.Clock()

# White color
white = (255, 255, 255)

# Green pipe image loaded using the pygame library
pipe_surface = pygame.transform.scale2x(pygame.image.load('images/pipe-green.png'))

# Pipe height list that determines the height of the pipes for
# random generation later
pipe_height = [300, 400, 600]

# Creating a new pygame event that will spawn pipes and set to trigger
# every 1200 millisecons or 1.2 seconds
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Creating a new pygame event named BIRDFLAP that will go through the bird
# images to make it seem like the bird is flapping its wings and set to trigger
# every 200 milliseconds or 0.2 seconds
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)


def main_menu():
    """
    This function will generate the main menu for the game where the user will be
    able to select from three different type of birds and play with that bird. To
    exit out the user can either click on the red x on the screen or click the escape
    button
    :return:
    """
    # Creating the main screen 574 pixels wide and 800 pixels high
    screen = pygame.display.set_mode((574, 800))
    # Setting the caption of the screen to FlappyBird
    pygame.display.set_caption('FlappyBird')
    # Creating UIScreen object names ui_screen
    ui_screen = UIScreen(screen)

    # Creating three bird objects, colored blue, red, and yellow using the bird class
    blue_bird = Bird('blue')
    red_bird = Bird('red')
    yellow_bird = Bird('yellow')

    # creating 3 buttons for the different colored birds
    red_bird_button = Button(250, 250, red_bird.bird_surface)
    blue_bird_button = Button(250, 100, blue_bird.bird_surface)
    yellow_bird_button = Button(250, 400, yellow_bird.bird_surface)

    while True:
        # Checking for pygame events to handle the appropriate user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Drawing the back ground of the game
        ui_screen.screen.blit(ui_screen.back_ground_surface, (0, 0))

        # Drawing the three buttons on the screen
        red_bird_button.draw_button()
        blue_bird_button.draw_button()
        yellow_bird_button.draw_button()

        # Getting the mouse position to handle when clicked
        mouse_position = pygame.mouse.get_pos()

        # Checking if the red bird button was clicked and calling the main_game function
        # with red as a parameter
        if red_bird_button.rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            main_game('red')

        # Checking if the blue bird button was clicked and calling the main_game function
        # with red as a parameter
        if blue_bird_button.rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            main_game('blue')

        # Checking if the yellow bird button was clicked and calling the main_game function
        # with red as a parameter
        if yellow_bird_button.rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            main_game('yellow')

        # Drawing the main menu text
        ui_screen.draw_text('Main Menu', ui_screen.game_font, white, ui_screen.screen, 20, 20)
        ui_screen.draw_text('High Score: ' + str(ui_screen.high_score), ui_screen.game_font, white, ui_screen.screen,
                            350, 20)
        ui_screen.draw_text('Pick your bird!', ui_screen.game_font, white, ui_screen.screen, ui_screen.width / 2 - 100,
                            60)

        pygame.display.update()


def main_game(bird_color):
    """
    This function handles all the main game events. A user will
    :param bird_color:
    :return:
    """
    screen = pygame.display.set_mode((574, 800))
    pygame.display.set_caption('FlappyBird')
    main_screen = UIScreen(screen)
    game_active = True

    main_bird = Bird(bird_color)

    pipe_list = []
    main_pipes = Pipe(pipe_list)
    game_over_rect = main_screen.game_over_surface.get_rect(center=(288, 350))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if main_screen.score > main_screen.high_score:
                    cursor.execute("UPDATE HighScore SET  highscore={} WHERE place=1".format(main_screen.score))
                db.commit()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    main_bird.bird_movement = 0
                    main_bird.bird_movement -= 9
                    main_bird.flap_sound()
                if event.key == pygame.K_ESCAPE:
                    main_menu()

                if event.key == pygame.K_SPACE and not game_active:
                    game_active = True
                    main_pipes.pipe_list.clear()
                    main_bird.bird_rect.center = (100, 400)
                    main_bird.bird_movement = 0
                    main_screen.score = 0

            if event.type == SPAWNPIPE:
                main_pipes.pipe_list.extend(main_pipes.create_pipe(pipe_surface, pipe_height))

            if event.type == BIRDFLAP:
                if main_bird.bird_index < 2:
                    main_bird.bird_index += 1
                else:
                    main_bird.bird_index = 0

                main_bird.bird_surface, main_bird.bird_rect = main_bird.bird_animation()

        main_screen.screen.blit(main_screen.back_ground_surface, (0, 0))

        if game_active:
            # Bird Handling
            main_bird.bird_movement += main_bird.gravity
            rotated_bird = main_bird.rotate_bird(main_bird.bird_surface)
            main_bird.bird_rect.centery += main_bird.bird_movement
            main_screen.screen.blit(rotated_bird, main_bird.bird_rect)
            game_active = main_bird.check_collision(main_pipes.pipe_list)

            # Pipe handling
            main_pipes.pipe_list = main_pipes.move_pipes(main_pipes.pipe_list, main_screen.score)
            main_pipes.draw_pipes(main_pipes.pipe_list, pipe_surface)

            # Handling Score
            for pipe in main_pipes.pipe_list:
                if pipe.centerx == 100:
                    main_screen.score += 1
                    main_bird.scoring_sound()
                    break

            main_screen.score_display('mainGame')
        else:
            main_screen.screen.blit(main_screen.game_over_surface, game_over_rect)
            main_screen.high_score = main_screen.update_score()
            main_screen.score_display('gameOver')
            if main_screen.score > main_screen.high_score:
                # database handling
                cursor.execute("UPDATE HighScore SET highscore={} WHERE place=1".format(main_screen.score))
                db.commit()

        main_screen.floor_x_pos -= 1
        main_screen.draw_floor()
        if main_screen.floor_x_pos <= -575:
            main_screen.floor_x_pos = 0

        pygame.display.update()
        clock.tick(120)


while True:
    main_menu()

pygame.quit()
