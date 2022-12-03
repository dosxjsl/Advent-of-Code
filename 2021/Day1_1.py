import re
import math
import random

file = open("Day1.txt").read().strip().splitlines()
file = [int(i) for i in file]

# ______________________FUNCTIONS______________________

# ______________________MAIN______________________
def main():
    increments = 0
    for i in range(len(file)):
        if file[i + 1] > file[i]:
            increments += 1
    print(increments)


if __name__ == "__main__":
    main()
