global screen
screen = 'start'
import levelScreen
def startGame():
    print('starting')
    global  screen
    screen = 'level'
    
def magnifyScroll(width, height):
    print('magnifying')
    levelScreen.scroll.width = width
    levelScreen.scroll.height = height
    print(width,height)
    levelScreen.scroll.x = width//2
    levelScreen.scroll.y = height//2
    
