import re
import math
import random

file = open("Day1.txt").read().strip().splitlines()
file = [int(i) for i in file]

# ______________________FUNCTIONS______________________


# ______________________MAIN______________________
def main():
    increments = 0
    for i in range(len(file) - 3):
        first3 = file[i] + file[i + 1] + file[i + 2]
        second3 = file[i + 1] + file[i + 2] + file[i + 3]
        if second3 > first3:
            increments += 1
    print(increments)


if __name__ == "__main__":
    main()
