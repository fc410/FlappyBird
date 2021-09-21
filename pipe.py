import pygame
import random

pygame.init()
screen = pygame.display.set_mode((574, 800))


class Pipe:
    # A list to put all the pipes in for handling in the future
    pipe_list = []

    def __init__(self, pipes):
        # Initiates the given list of pipes to the objects pipe_list
        self.pipe_list = pipes

    @staticmethod
    def draw_pipes(pipes, pipe_surface):
        """
        This function draws the given pipe surface in the given location
        of the pipe list
        :param pipes: I list of pipes that have been created already
        :param pipe_surface: I pipe surface or image loaded in using the pygame
                             library
        :return: two pipes on inverted as the other to make a small window
                 where the bird can fly through
        """
        for pipe in pipes:
            if pipe.bottom >= 800:
                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)

    @staticmethod
    def create_pipe(pipe_surface, pipe_height):
        """
        This function creates a pipe from the given pipe surface or image
        loaded in using the pygame library with a random height from the given
        pipe_height list
        :param pipe_surface: An image loaded in using the pygame library
        :param pipe_height: A pipe height list to randomly choose from
        :return: returns a bottom pipe with a random height from the given pipe
                 height list and a top pipe from the random pipe height - 250
                 to give the bird a small window to jump through
        """
        random_pipe_pos = random.choice(pipe_height)
        bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
        top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 250))
        return bottom_pipe, top_pipe

    @staticmethod
    def move_pipes(pipes, score):
        """
        This function moves the pipes at 5 pixels per frames to make its
        seem like the pipes are moving and increases the score if the pipes
        is equal to 90 pixels
        :param pipes: A list of pipes to move all the pipes in the list
        :param score: An integer value that shows the current score of the player
        :return: Returns the pipe list with all pipes moved 5 pixels to the left
        """
        for pipe in pipes:
            pipe.centerx -= 5
            if pipe.centerx == 90:
                score += 1
        return pipes
