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


def noDuplicates(arr):
    if len(arr) == len(list(set(tuple(sub) for sub in arr))):
        return True
    else:
        return False


def redistribute(input):

    occurSet = []
    redistributionCycles = 0

    while noDuplicates(occurSet):
        largestNum = largest(input)[0]
        largestIndex = largest(input)[1]

        input[largestIndex] = 0
        nextIndex = largestIndex + 1
        counter = 0
        redistributionCycles += 1

        # redistrbute number until unable to
        while counter < largestNum:
            # if it reaches the end, loop back to start
            if nextIndex >= len(input):
                nextIndex = 0
            else:
                input[nextIndex] += 1
                counter += 1
                nextIndex += 1
            if counter == largestNum:
                occurSet.append(input.copy())

    extra = len(occurSet) - occurSet.copy().index(occurSet[-1])
    return redistributionCycles, extra


# ______________________MAIN______________________
def main():

    FILE = [int(i) for i in open("D6.txt", "r").read().split("\t")]

    print(redistribute(FILE))


if __name__ == "__main__":
    main()
