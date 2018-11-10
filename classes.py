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

def tasks():
    d = {"Begin or continue writing a book": [30, False], "Explore the city": [10, False], "Go kayaking": [15, False],
           "Go rock climbing": [10, False], "Go diving": [20, False], "Wake up at 5am": [10, False],
           "Paint a picture": [15, False], "Go to the gym": [5, False], "Eat healthy food": [5, False],
           "Write down 3 good things that happened to you": [5, False], "Exercise": [5, False],
           "Call an old friend": [5, False], "Take a nap": [10, False], "Talk to a stranger": [10, False],
           "Take a walk in the woods": [10, False], "Introduce yourself to someone new": [15, False],
           "Park in the farthest parking spot": [5, False], "Do not eat fast food": [10, False],
           "Drink 8 cups of water today": [10, False], "Read": [5, False], "Listen to music": [5, False],
           "Reduce, reuse, and recycle": [20, False]}
    return d

def makeTaskList(lst, task):
    lst.append(task)
    return lst

import random
def addRandomTask(d, taskList):
    lst = list(d)
    task = random.choice(lst)
    taskList.append(task)
    return taskList


def dictTask(taskList, d):
    # turns tasklist into a dictionary with the hunger points
    taskDict = {}
    for task in taskList:
        taskDict[task] = d[task]
    return taskDict


class Statsbar(object):
    def __init__(self, level, x, y):
        self.level = level
        self.x = x
        self.y = y

    def draw(self, surface):
        pass




