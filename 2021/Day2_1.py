import re
import math
import random

file = open("test.txt").read().strip().splitlines()

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
    # depth, horizontal
    position = [0, 0]
    directions = genDirections(file)

    # print(directions)

    for direction in directions:
        path = direction[0]
        steps = int(direction[1])
        if path == "forward":
            position[1] += steps
        elif path == "down":
            position[0] += steps
        elif path == "up":
            position[0] -= steps
    print(position)
    print(position[0] * position[1])


if __name__ == "__main__":
    main()
