from random import choice
from getkey import getkey
import time
import numpy as np
import sys

if sys.argv[1] == "ones":
    nums = list(range(10))
elif sys.argv[1] == "left":
    nums = list(range(1, 6))
elif sys.argv[1] == "right":
    nums = [0] + list(range(6, 10))
else:
    print("Usage: python3 num_game.py [ones, left, or right]")
    sys.exit(1)

times = []

time.sleep(1)

mistakes = 0
for _ in range(20):
    tick = time.time()
    n = choice(nums)
    print(n)
    m = -1

    while True:
        m = int(getkey())
        if m == n:
            break
        else:
            mistakes += 1
    tock = time.time()

    times.append(tock - tick)

print("Average response time: " + str(np.mean(times)))
print("Total time: " + str(sum(times)))
print("Mistakes: " + str(mistakes))