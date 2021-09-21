# This file contains the UIScreen class for the main screen
# to draw or write in the flappy bird game
import pygame
from database import cursor, db

cursor.execute("SELECT * FROM highscore")
high_score_list = []
for row in cursor:
    high_score_list.append(row)


class UIScreen:
    # loading the back ground surface for later use
    back_ground_surface = pygame.transform.scale(
        pygame.image.load('images/background-day.png'), (574, 800)
    ).convert_alpha()

    # loading the floor surface for later use
    floor_surface = pygame.transform.scale2x(
        pygame.image.load('images/base.png')
    ).convert_alpha()

    # floor position to make it look like the floor surface is
    # moving
    floor_x_pos = 0

    game_over_surface = pygame.transform.scale2x(
        pygame.image.load('images/message.png')
    )

    # loading in the game font for the whole game
    game_font = pygame.font.SysFont('04B_19.TTF', 40)

    # Game instance to determine if the player is playing the main
    # game
    game_active = True

    # variables for the score and high score to be used in the game
    score = 0
    high_score = high_score_list[0][1]

    def __init__(self, screen):
        """
        This constructor initializes the given screen and initilizes
        the width and height from the given screen
        :param screen: a pygame screen to be able to draw images using
                       the pygame library
        """
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

    def draw(self, image, x, y):
        """
        This function draws a given image at a given x and y location
        in the object sreeen
        :param image: an image that has been loaded in using the pygame library
        :param x: An x location to draw the given image on
        :param y: A y location to draw the given image on
        :return:
        """
        self.screen.blit(image, (x, y))

    @staticmethod
    def draw_text(text, font, color, surface, x, y):
        """
        :param text: Specifies what text you want to be written
        :param font: Specifies what font type you want your text to be
        :param color: Specifies the color you want your text to be, can be a tuple or variable
        :param surface: Specifies the surface or screen you want the text to be written on
        :param x: Specifies the x value you want the text to be in the surface/screen
        :param y: Specifies the y value you want the text to be in the surface/screen
        :return: returns text on the surface/screen in the specified x and y value with
                 the given font, and color
        """
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def draw_floor(self):
        """
        This Function draws two floor surface images next to each other
        so that when one surface goes out of range from the screen width
        the other surface shows
        :return: two floor surfaces next to each other so that it looks
                 like the floor is never ending
        """
        self.screen.blit(self.floor_surface, (self.floor_x_pos, 700))
        self.screen.blit(self.floor_surface, (self.floor_x_pos + 576, 700))

    def update_score(self):
        """
        This function updates the high_score only if score is greater
        than the high score
        :return: an updated high score both in game and in the database
        """
        if self.score > self.high_score:
            self.high_score = self.score
            cursor.execute("UPDATE HighScore SET highscore={} WHERE place=1".format(self.score))
            db.commit()
        return self.high_score

    def scoring(self, pipes):
        """
        Updates the score if the bird rect passes through the pipes in
        the given pipe list
        :param pipes: A pipe list that cointains all the pipes in the
                      game
        :return: An updated score if the pipes.centerx is less than or
                 equal to 400
        """
        for pipe in pipes:
            if pipe.centerx <= 400:
                self.score += 1

    def score_display(self, game_state):
        """
        This function draws text of the score display for the appropriate
        game state in the objects screen
        :param game_state: A string variable that states if the player is
                           either in the main game, main menu, or in the game
                           over game
        :return:
        """
        if game_state == 'mainGame':
            score_surface = self.game_font.render(('Score: ' + str(int(self.score))), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 50))
            self.screen.blit(score_surface, score_rect)
        if game_state == 'gameOver':
            score_surface = self.game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 50))
            self.screen.blit(score_surface, score_rect)

            high_score_surface = self.game_font.render(
                ('High Score: ' + str(int(self.high_score))), True, (255, 255, 255)
            )
            high_score_rect = high_score_surface.get_rect(center=(288, 650))
            self.screen.blit(high_score_surface, high_score_rect)

        if game_state == 'mainMenu':
            pass
