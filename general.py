import buttons
class Surface(object):
    drawList = []
    def __init__(self):
        Surface.drawList.append(self)
        
    @staticmethod
    def clear():
        Surface.drawList = []
        
    def bringForward(self):
        Surface.drawList.remove(self)
        Surface.drawList.append(self)

class Rectangle(Surface):
    def __init__(self, pygame, x, y, width, height, color):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surf = pygame.Surface((width, height))
        if color != None:
            self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.pygame = pygame
    
    def pointInRect(self, x, y):
        return (self.x-self.width//2 <= x <= self.x+self.width//2) and (self.y-self.height//2 <= y <= self.y+self.height//2)
        
    def draw(self, screen):
        if self.color != None:
            screen.blit(self.surf, (self.x-self.width//2, self.y-self.height//2))
        
class Button(Rectangle):
    buttonList = []
    def __init__(self, pygame, x, y, width, height, color, text, functionString, fontColor=(0,0,0)):
        super().__init__(pygame, x, y, width, height, color)
        self.text = text
        self.function = functionString
        Button.buttonList.append(self)
        self.fontColor = fontColor
        
        
    def onClick(self):
        print('running')
        if self.function != 'pass':
            eval('buttons.'+self.function)
        
    def checkClick(self, x, y):
        print('checking', x, y)
        if self.pointInRect(x, y):
            self.onClick()
            
    def draw(self, screen):
        super().draw(screen)
        font = self.pygame.font.Font('freesansbold.ttf',18)
        surf = font.render(self.text, True, self.fontColor)
        rect = surf.get_rect()
        rect.center = ((self.x, self.y))
        screen.blit(surf, rect)

class Image(Surface):
    def __init__(self, pygame, x, y, width, height, image):
        super().__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.pygame = pygame
        self.width = width
        self.height = height
        
    def draw(self, screen):
        self.surf = self.pygame.transform.scale(self.surf, (self.width, self.height))
        screen.blit(self.surf, (self.x-self.width//2, self.y-self.height//2))
# 
# class BlinkingRectangle(Rectangle):
#     def __init__(self, pygame, x, y, width, height, color, period):
#         super().__init__(pygame, x, y, width, height, color)
#         self.period = period
#         self.calls = 0
#         
#     def draw(self, screen):
#         self.calls += 1
#         if self.calls/self.period % 2 < 1:
#             super().draw(screen)
        
def checkButtons(x, y):
    for button in Button.buttonList:
        button.checkClick(x, y)
            
def drawAll(screen):
    for item in Surface.drawList:
        item.draw(screen)
        
def test():
    print('yay')