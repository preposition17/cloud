import os
import time

filenames = os.listdir("ilnaz_data")
filenames = [int(i) for i in filenames]

now = int(time.time())


def nearest(lst, target):
    return min(lst, key=lambda x: abs(x - target))


for i in range(now - 3600, now, 60):
    print(nearest(filenames, i))
