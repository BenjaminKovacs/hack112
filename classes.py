class Pet(object):
    def __init__(self, name, x, y, img):
        self.name = name
        self.x = x
        self.y = y
        self.hunger = 50
        self.img = img

    def eat(self, food):
        self.hunger -= food

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def angerLevel(self):
        return self.hunger % 20

    def getImage(self):
        return self.img

    def draw(self, surface):
        pass

class Task(object):
    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return str(self.task)

class Statsbar(object):
    def __init__(self, level, x, y):
        self.level = level
        self.x = x
        self.y = y

    def draw(self, surface):
        pass




