global screen
global exitImage
global exitButton
global buttonList
global tasksCompleted 
tasksCompleted = 0
buttonList = []
screen = 'start'
import levelScreen
import general
def startGame():
    print('starting')
    global  screen
    screen = 'level'

def cat():
    print('cat')

def exit():
    try:
        print('exit')
        global buttonList
        for button in buttonList:
            try:
                button.destroy()
            except:
                pass
    except:
        pass
    try:
        global exitButton
        exitButton.destroy()
    except:
        pass
    try:
        levelScreen.scroll.reset()
    except:
        pass
    try:
        global exitImage
        exitImage.destroy()
    except:
        pass

def removeFromList(task, button):
    try:
        global buttonList
        buttonList[button].destroy()
        global tasksCompleted
        tasksCompleted += 1
        result = []
        fileContents = ""
        for line in levelScreen.readFile("Tasks.txt").split('\n'):
            if line != task:
                result.append(line)
        for line in result:
            fileContents += line + '\n'
        levelScreen.writeFile("Tasks.txt", fileContents)
    except:
        pass
            
    
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
    
    n = 0
    global buttonList
    for line in levelScreen.readFile("Tasks.txt").split('\n'):
        if line != "":
            n+=1
        buttonList.append(general.Button(levelScreen.scroll.pygame, width//2, 100+50*n, width, 50, None, line, 'removeFromList("'+line+'",'+str(len(buttonList))+')'))

        
    
    

