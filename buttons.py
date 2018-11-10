global screen
global exitImage
global exitButton
screen = 'start'
import levelScreen
import general
def startGame():
    print('starting')
    global  screen
    screen = 'level'

def exit():
    print('exit')
    levelScreen.scroll.reset()
    global exitImage
    exitImage.destroy()
    global exitButton
    exitButton.destroy()
    
def magnifyScroll(width, height):
    print('magnifying')
    levelScreen.scroll.width = width
    levelScreen.scroll.height = height
    levelScreen.scroll.x = width//2
    levelScreen.scroll.y = height//2
    global exitImage
    exitImage = general.Image(levelScreen.scroll.pygame, 50,50,100,100,'images/exit.jpg')
    global exitButton
    exitButton = general.Button(levelScreen.scroll.pygame, 50,50,100,100,None,'','exit()')
    
    for line 
    
    