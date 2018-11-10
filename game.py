import module_manager
module_manager.review()

#https://realpython.com/pygame-a-primer/
# import the pygame module
import pygame
import general
import startScreen
# import pygame.locals for easier access to key coordinates
from pygame.locals import *

# Define our player object and call super to give it all the properties and methods of pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))

# instantiate our player; right now he's just a rectangle
player = Player()
startScreen.createScreen(pygame, width, height)
# Variable to keep our main loop running
running = True

# Our main loop!
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            general.checkButtons(x, y)
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False

    # Draw the player to the screen
    general.drawAll(screen)
    # Update the display
    pygame.display.flip()