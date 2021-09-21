import pygame
from screen import UIScreen

screen = pygame.display.set_mode((574, 800))


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw_button(self):
        """
        This function draws a button on the screen
        :return: a button drawn on the screen
        """

        ui_screen = UIScreen(screen)
        ui_screen.screen.blit(self.image, (self.rect.x, self.rect.y))

