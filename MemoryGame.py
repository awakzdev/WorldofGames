import time
import os
import random


def memory_game(diff):
    x = random.sample(range(101), diff * 2)
    print(x)

    print('Remember us')

    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')

    y = [int(y) for y in input(f"Do you remember your {diff * 2} numbers?\n"
                               f"Rules are! no commas and spaces between each number :").split()]

    print(f"your list was: {x}")
    print(f"you entered: {y}")
    if x == y:
        print("True!")
        return True
    else:
        print("False!")
        return False
