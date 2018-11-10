import module_manager
module_manager.review()

#https://realpython.com/pygame-a-primer/
# import the pygame module
import pygame
import os
import general
import buttons
import startScreen
import levelScreen
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

# # Our main loop!
# while running:
#     # for loop through the event queue
#     for event in pygame.event.get():
#         x, y = pygame.mouse.get_pos()
#         if event.type == MOUSEBUTTONDOWN:
#             general.checkButtons(x, y)
#         # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
#         if event.type == KEYDOWN:
#             # If the Esc key has been pressed set running to false to exit the main loop
#             if event.key == K_ESCAPE:
#                 running = False
#         # Check for QUIT event; if QUIT, set running to false
#         elif event.type == QUIT:
#             running = False
# 
#     # Draw the player to the screen
#     general.drawAll(screen)
#     # Update the display
#     pygame.display.flip()
    
class PygameGame(object):
    oldScreen = 'start'
    def init(self):
        self.timeSkip = 0
        self.cat = pygame.image.load(os.path.join('Images/pet.png'))
        self.displayCat = pygame.transform.scale(self.cat, (100, 100))
        self.catDimensions = self.cat.get_size()
        self.taskIcon = pygame.transform.scale(pygame.image.load(os.path.join('images/task_icon.png')), (100,100))
        self.scroll = pygame.transform.scale(pygame.image.load(os.path.join('images/scroll.png')), (100,100))
        self.Task = False
        self.mainGame = False
        startScreen.createScreen(pygame, self.width, self.height)
        pygame.mixer.music.load('hack112_music.wav')
        pygame.mixer.music.play(-1)

    def mousePressed(self, x, y):
        general.checkButtons(x, y)
        if self.mainGame:
            if x in range(0, 100) and y in range(self.height - 100, self.height):
                self.Task = True
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        print(keyCode)
        print(chr(keyCode))
        if self.mainGame:
            if keyCode == 27:
                self.Task = False
                self.scroll = pygame.transform.scale(pygame.image.load(os.path.join('images/scroll.png')), (100,100))
        levelScreen.textString(pygame, self.width, self.height, keyCode)
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        screen = buttons.screen
        if screen != PygameGame.oldScreen:
            general.Surface.clear()
            eval(screen+'Screen.createScreen(pygame, self.width, self.height)')
            PygameGame.oldScreen = screen

    def redrawAll(self, screen):
        if self.mainGame == True:
            a = pygame.draw.rect(screen, (128,128,128), pygame.Rect(0, self.height-100, self.width, 100))
            # a = pygame.Surface((self.width, 100))
            # a.fill((128,128,128))
            screen.blit(self.displayCat, (self.width//2 - 100, self.height - 300))
            screen.blit(self.taskIcon, (0, self.height-100))
            if not self.Task:
                screen.blit(self.scroll, (self.width//2 + 50, self.height - 300))
            if self.Task:
                self.scroll = pygame.transform.scale(self.scroll, (self.height - 100, self.width - 100))
                screen.blit(self.scroll, (self.width//2, 0))
        general.drawAll(screen)
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=1000, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()