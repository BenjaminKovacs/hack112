import general
import classes
import levels
def createScreen(pygame, width, height):
    general.Image(pygame, width//2, height//2, width, height, 'images/pictures.jpg')
    general.Image(pygame, width//2, 2*height//3, width//5, height//5, 'images/cat.png')