import time
import random
import math
from tqdm import tqdm
import matplotlib.pyplot as plt



def get_noise():
    x1 = random.uniform(0, 10)
    x2 = random.uniform(0, 10)
    x3 = random.uniform(0, 10)

    while True:
        sin1 = 2 * math.sin(x1) + 2
        sin2 = 0.2 * math.sin(x2)
        sin3 = 0.2 * math.sin(x3)
        x1 += 0.001
        x2 += 0.01 + random.uniform(0, 0.0001)
        x3 += 0.01 + random.uniform(0, 0.0001)


        yield sin1 + sin2 + sin3 + random.uniform(0, 0.5)




t = get_noise()
h = get_noise()
for i in tqdm(range(3600)):
    with open(f"ilnaz_data/{int(time.time())-i}", "w") as file:
        file.write(f"t{next(t) + 25}\n"
                   f"h{next(h) + 10}\n"
                   f"b{random.choice([0, 1])}")



