import re
import math

# ______________________FUNCTIONS______________________
def largest(array):
    max = array[0]
    index = 0
    for i in range(len(array) - 1):
        if array[i + 1] > max:
            max = array[i + 1]
            index = i + 1
    return max, index


def redistribute(input):

    occurSet = []

    while input not in occurSet:
        occurSet.append(input.copy())

        largestNum = largest(input)[0]
        largestIndex = largest(input)[1]

        input[largestIndex] = 0

        # redistrbute number until unable to
        while largestNum:
            # if it reaches the end, loop back to start
            largestIndex = (largestIndex + 1) % len(input)
            input[largestIndex] += 1
            largestNum -= 1

    return len(occurSet)


# ______________________MAIN______________________
def main():

    FILE = [int(i) for i in open("D6.txt", "r").read().split("\t")]

    print(redistribute(FILE))


if __name__ == "__main__":
    main()
