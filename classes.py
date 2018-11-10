import general
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
        return self.hunger // 20

    def getImage(self):
        return self.img

    def draw(self, surface):
        pass

class Tasks(object):
    def __init__(self, taskList, img, x, y):
        self.taskList = taskList
        self.img = img
        self.x = x
        self.y = y

    def addTask(self, task):
        self.taskList.append(task)

    def draw(self):
        # draw image
        fontSize = len(self.img)//len(self.taskList)
        for i in range(len(self.taskList)):
            # create text len(img[0])//2, y*(fontSize*i)+margin
            pass

    def __repr__(self):
        return str(self.taskList)

class Statsbar(object):
    def __init__(self, level, x, y):
        self.level = level
        self.x = x
        self.y = y

    def draw(self, surface):
        pass




