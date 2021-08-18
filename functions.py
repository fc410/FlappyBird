import pygame
import random
import images
import sys
import bird
import scoring
import variableDatabase

def drawText(text, font, color, surface, x, y):
    """

    :param text: Specifies what text you want to be written
    :param font: Specifies what font type you want your text to be
    :param color: Specifies the color you want your text to be, can be a tuple or varialbe
    :param surface: Specifies the surface or screen you want the text to be written on
    :param x: Specifies the x value you want the text to be in the surface/screen
    :param y: Specifies the y value you want the text to be in the surface/screen
    :return: returns text on the surface/screen in the specified x and y value with
             the given font, and color
    """
    textObj = font.render(text, 1, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObj, textRect)


def draw_floor():
    images.screen.blit(images.floor_surface, (images.floor_x_pos, 700))
    images.screen.blit(images.floor_surface, (images.floor_x_pos + 576, 700))


def main_menu():
    while True:
        # draws the images into the screen
        images.screen.blit(images.back_ground_surface, (0, 0))

        blue_bird_surface = bird.blueBird.get_rect(center=(images.width/2 - 30, 100))
        red_bird_surface = bird.redBird.get_rect(center=(images.width / 2 - 30, 250))
        yellow_bird_surface = bird.yellowBird.get_rect(center=(images.width / 2 - 30, 400))

        images.screen.blit(bird.blueBird, (images.width/2 - 30, 100))
        images.screen.blit(bird.redBird, (images.width / 2 - 30, 250))
        images.screen.blit(bird.yellowBird, (images.width / 2 - 30, 400))

        drawText('Main Menu', images.font, images.white, images.screen, 20, 20)
        drawText('High Score: ' + str(scoring.high_score), images.font, images.white, images.screen, 400, 20)
        drawText('Pick your bird!', images.font, images.white, images.screen, images.width/2 - 50 , 50)

        # buttons
        #pygame.draw.rect(images.screen, images.white, (150,450, 100,50))
        mouseX, mouseY = pygame.mouse.get_pos()

        if blue_bird_surface.collidepoint(mouseX,mouseY):
            if click:
                return "blue bird"

        if red_bird_surface.collidepoint(mouseX,mouseY):
            if click:
                return "red bird"

        if yellow_bird_surface.collidepoint(mouseX,mouseY):
            if click:
                return "yellow bird"


        #button1 = pygame.rect(50,100, 200, 50)
        #button2 = pygame.rect(50,200, 200, 50)
        #button3 = pygame.rect(50,300, 200, 50)

        # collisions  for the buttons
        #if button1.collidepoint(mouseX, mouseY):
        #    if click:
        #        pass
        #if button2.collidepoint(mouseX, mouseY):
        #    if click:
        #        pass
        #if button3.collidepoint(mouseX, mouseY):
        #    if click:
        #        pass
        #pygame.draw.rect(screen, (255,0,0), button1)
        #pygame.draw.rect(screen, (255, 0, 0), button2)
        #pygame.draw.rect(screen, (255, 0, 0), button3)

        click = False
        # handling game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True



        pygame.display.update()




# initializes pygame
pygame.init()


