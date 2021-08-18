import pygame
import sys
import functions
import images
from variableDatabase import cursor, db
import bird
import pipe
import scoring

# loop to keep the screen from closing
while True:
    # gets any event triggered from the user
    for event in pygame.event.get():
        # checking to see if the user exits the screen
        if event.type == pygame.QUIT:
            if scoring.score > scoring.high_score:
                cursor.execute("UPDATE HighScore SET  highscore={} WHERE place=1".format(scoring.score))
                db.commit()
            # close the display and quit the game
            pygame.quit()
            # shuts down the game completely
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and images.game_active:
                bird.bird_movement = 0
                bird.bird_movement -= 9
                bird.flap_sound.play()
            if event.key == pygame.K_ESCAPE:
                functions.main_menu()

            if event.key == pygame.K_SPACE and not images.game_active:
                images.game_active = True
                pipe.pipe_list.clear()
                bird.bird_rect.center = (100, 400)
                bird.bird_movement = 0
                scoring.score = 0

        if event.type == pipe.SPAWNPIPE:
            pipe.pipe_list.extend(pipe.create_pipe())

        if event.type == bird.BIRDFLAP:
            if bird.bird_index < 2:
                bird.bird_index += 1
            else:
                images.bird_index = 0

            images.bird_surface, images.bird_rect = bird.bird_animation()

    # puts the back ground image in the specified location
    images.screen.blit(images.back_ground_surface, (0, 0))

    if images.game_active:
        # bird handling
        bird.bird_movement += bird.gravity
        rotated_bird = bird.rotate_bird(bird.bird_surface)
        bird.bird_rect.centery += bird.bird_movement
        images.screen.blit(rotated_bird, bird.bird_rect)
        images.game_active = bird.check_collision(pipe.pipe_list)

        # pipe handling
        pipe.pipe_list = pipe.move_pipes(pipe.pipe_list, scoring.score)
        pipe.draw_pipes(pipe.pipe_list)

        # handling score
        for pip in pipe.pipe_list:
            if pip.centerx == 100:
                scoring.score += 1
                scoring.score_sound.play()
                break

        scoring.score_display('mainGame')

    else:
        images.screen.blit(images.game_over_surface, images.game_over_rect)
        scoring.high_score = scoring.update_score(scoring.score, scoring.high_score)
        scoring.score_display('gameOver')
        if scoring.score > scoring.high_score:
            cursor.execute("UPDATE HighScore SET highscore={} WHERE place=1".format(scoring.score))
            db.commit()

    # floor handling
    images.floor_x_pos -= 1
    functions.draw_floor()
    if images.floor_x_pos <= -575:
        images.floor_x_pos = 0

    # updates the screen with any logic specified before
    pygame.display.update()

    # will never run faster than 120 frames per second
    images.clock.tick(120)

# Closes the display
pygame.quit()
