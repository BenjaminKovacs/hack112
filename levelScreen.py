import general
import classes
import levels
import string
text = None
global textDisplay

def addAndDisplay(text):
    pass

def run(text):
    try:
        eval(text)
    except:
        addAndDisplay(text)
        

def createScreen(pygame, width, height):
    global textDisplay
    textDisplay = general.Button(pygame, 0,0,0,0, None, '', 'pass', (255,255,255))
    general.Image(pygame, width//2, height//2, width, height, 'images/pictures.jpg')
    general.Image(pygame, width//3.1, 2*height//3, width//5, height//5, 'images/task list.png')
    general.Image(pygame, width//2, 2*height//3, width//5, height//5, 'images/cat.png')
    
def textEntry(pygame, width, height, text):
    global textDisplay
    letterWidth = 1.4
    textDisplay = general.Button(pygame, 0,0,0,0, None, '', 'pass', (255,255,255))
    print('yay')
    general.Rectangle(pygame, width//2, 40*height//50, width, height//25, (0,0,0))
    # general.BlinkingRectangle(pygame, letterWidth*width//100 * len(text), 40*height//50, width//100, height//25-3, (255,255,255), 5)
    textDisplay.bringForward()
    textDisplay.text = text
    textDisplay.x = letterWidth*width//200 * len(text)
    textDisplay.y = 40*height//50
    textDisplay.width = letterWidth*width//100 * len(text)
    textDisplay.height = height//25-3
    
def textString(pygame, width, height, char):
    global text
    if char == 271 or char == 13:
        if text != None:
            run(text)
        text = ""
        textEntry(pygame, width, height, text)
    elif text != None:
        # if chr(char) in ("." , "," , " ", "a" ,"b","c","d","e","f","g","h","i"):
        if chr(char) in string.ascii_letters or chr(char) in string.digits or\
        chr(char) == " " or chr(char) == "." or chr(char) == ",":
            text += chr(char)
            textEntry(pygame, width, height, text)
        if char == 8:
            text = text[:len(text)-1]
            textEntry(pygame, width, height, text)
    
    