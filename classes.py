class Pet(object):
    def __init__(self, name, animal, x, y):
        self.name = name
        self.animal = animal
        self.x = x
        self.y = y
        self.hunger = 50

    def eat(self, food):
        self.hunger -= food

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return (str(self.name), str(self.animal), self.x, self.y)


        