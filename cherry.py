import random

class Cherry:
    def __init__(self, snake, xlim, ylim):
        touch = True
        while touch:
            touch = False
            self.x = random.randint(0,xlim)
            self.y = random.randint(0,ylim)
            for a in snake.body:
                if self.x == a[0] and self.y == a[1]:
                    touch = True