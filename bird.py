import pygame

pygame.init()
screen = pygame.display.set_mode((574, 800))


class Bird:
    # Bird variables for handling later
    bird_movement = 0
    gravity = 0.25
    bird_index = 0
    score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
    bird_frames = []

    def __init__(self, bird_color):
        """
        This constructor initializes a bird object from the given color
        and loads in the down, mid, and top flap from the given color and
        scales the bird 2x. It also initializes the bird frames list with
        a list of the three images loaded, bird surfaces as the list of these
        birds, and bird rect as the rect of the bird surfaces.
        :param bird_color: A string of either red, blue, or yellow to create
                           a specific bird
        """
        # Upload the up, mid, and down flap images
        up_color = 'images/' + bird_color.lower() + 'bird-upflap.png'
        mid_color = 'images/' + bird_color.lower() + 'bird-midflap.png'
        down_color = 'images/' + bird_color.lower() + 'bird-downflap.png'

        # Scale the images 2x
        bird_down_flap = pygame.transform.scale2x(
            pygame.image.load(down_color).convert_alpha())
        bird_mid_flap = pygame.transform.scale2x(
            pygame.image.load(mid_color).convert_alpha())
        bird_up_flap = pygame.transform.scale2x(
            pygame.image.load(up_color).convert_alpha())

        # Initiate all the object variables
        self.bird_frames = [bird_down_flap, bird_mid_flap, bird_up_flap]
        self.bird_color = bird_color
        self.bird_surface = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird_surface.get_rect()

    @staticmethod
    def death_sound():
        """
        This fuction loads in the mixer sound using the pygame library
        and plays the sound
        :return: The audio of the loaded sound
        """
        # Load in the die sound effect
        death_sound = pygame.mixer.Sound('sound/sfx_die.wav')
        # play the death sound effect
        death_sound.play()

    @staticmethod
    def flap_sound():
        """
        This function loads in the mixer sound of the wing flapping sound
        effect and plays the sound
        :return: The audio of the loaded wing flapping sound
        """
        # Load in the wing flapping sound
        flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
        # Play the flappng sound effect
        flap_sound.play()

    def check_collision(self, pipes):
        """
        This function checks to see if the bird has collided with any
        of the pipes from the pipe list
        :param pipes: A list of pipes to check the collision from
        :return: A boolean value; false if the bird did collide with
                 one of the pipes or true otherwise
        """
        for pipe in pipes:
            # If the bird collides with one of the pipes return false
            # and play the death sound
            if self.bird_rect.colliderect(pipe):
                self.death_sound()
                return False

        # If the bird goes above a certain value and hits the roof
        # or if the bird goes to low and hits the bottom then return
        # false and play the death sound
        if self.bird_rect.top <= -100 or self.bird_rect.bottom >= 750:
            self.death_sound()
            return False

        return True

    def bird_animation(self):
        """
        This function a new bird and bird rect to make it seem like the
        bird is flapping its wings
        :return: a new bird and bird rect to make it seem like the bird
                 flapping its wings
        """
        new_bird = self.bird_frames[self.bird_index]
        new_bird_rect = new_bird.get_rect(center=(100, self.bird_rect.centery))
        return new_bird, new_bird_rect

    def rotate_bird(self, bird):
        """
        This function rotates the bird to make it seem like its moving
        :param bird: An image of a bird to rotate
        :return: a rotated bird of the given bird
        """
        new_bird = pygame.transform.rotozoom(bird, -self.bird_movement * 3, 1)
        return new_bird

    def scoring_sound(self):
        """
        This function plays the scoring sound
        :return: The sound of the scoring sound that was loaded in
        """
        self.score_sound.play()
