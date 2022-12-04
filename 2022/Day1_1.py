import re
import math
import random

file = open("D1.txt").read().strip().splitlines()
# file = [int(i) for i in file]

# ______________________FUNCTIONS______________________
def getElves(input):
    elfList = []
    elf = []
    for line in input:
        if line != "":
            line = int(line)
            elf.append(line)
        else:
            elfList.append(elf)
            elf = []
    elfList.append(elf)
    return elfList


# ______________________MAIN______________________
def main():
    elves = getElves(file)
    max = 0
    for i in elves:
        elfTotals = sum(i)
        if elfTotals > max:
            max = elfTotals
    print(max)


if __name__ == "__main__":
    main()
