import re
import math
import random

file = open("D1.txt").read().strip().splitlines()

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
    allElves = []
    for i in elves:
        allElves.append(sum(i))

    allElves.sort(reverse=True)

    top3 = 0
    for i in range(3):
        print(allElves[i])
        top3 += allElves[i]
    print(top3)


if __name__ == "__main__":
    main()
