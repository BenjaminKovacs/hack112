import general
import classes
def createScreen(pygame, width, height):
    buttonSpace = 70
    #general.Button(pygame, width//2, height//3, width//4, height//20, (0,255,0), 'Start game','startGame()')
    #general.Button(pygame, width//2, height//3+buttonSpace, width//4, height//20, (255,0,0), 'Red button','startGame()')
    #general.Button(pygame, width//2, height//3+2*buttonSpace, width//4, height//20, (0,0,255), 'Blue button','startGame()')
    general.Button(pygame, 276, 449, 260, 67, None, 'Blank button','startGame()')
    general.Image(pygame, width//2, height//2, width, height, 'images/startScreen.jpg')