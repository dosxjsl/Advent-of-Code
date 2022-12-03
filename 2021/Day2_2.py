import re
import math
import random

file = open("Day2.txt").read().strip().splitlines()

# ______________________FUNCTIONS______________________
# def genDirections(input):
#     whole = []
#     eachThing = {}
#     for line in input:
#         line = line.split(" ")
#         for i in range(len(line) - 1):
#             eachThing[line[0]] = line[1]
#         whole.append(eachThing)
#         eachThing = {}
#     return whole
def genDirections(input):
    whole = []
    eachThing = []
    for line in input:
        line = line.split(" ")
        for i in range(len(line)):
            eachThing.append(line[i])
        whole.append(eachThing)
        eachThing = []
    return whole


# ______________________MAIN______________________
def main():
    depth = 0
    horizontal = 0
    aim = 0
    directions = genDirections(file)

    for direction in directions:
        path = direction[0]
        steps = int(direction[1])

        if path == "forward":
            horizontal += steps
            depth += aim * steps
        elif path == "down":
            aim += steps
        elif path == "up":
            aim -= steps

    print(horizontal * depth)


if __name__ == "__main__":
    main()
