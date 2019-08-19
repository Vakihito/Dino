import operator
from random import randint
from random import choice
import operator

class te(object):
        def __init__(self, x = 4, y = 3, n = 'd'):
                self.x = x
                self.y = y
                self.name = n

new = [te() for i in range(10)]

i = 0
swt = { 0 : new[i].x, 1 : new[i].y}

for i in range(len(new)):
        swt[i % 2] = 0

print([(i.x, i.y) for i in new])