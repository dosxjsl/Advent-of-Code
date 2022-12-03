import re
import math
import random


# ______________________FUNCTIONS______________________
def getMoveList(input):
    moves = []
    for line in input:
        if line != "":
            line = line.split()
            moves.append(line)
        else:
            moves.append(moves)
    return moves


def outcomes(opponent, you):
    score = 0

    win = 6
    draw = 3
    lose = 0

    rock = 1
    paper = 2
    scissors = 3

    if opponent == "A":
        if you == "X":
            score += scissors + lose
        elif you == "Y":
            score += rock + draw
        elif you == "Z":
            score += paper + win

    elif opponent == "B":
        if you == "X":
            score += rock + lose
        elif you == "Y":
            score += paper + draw
        elif you == "Z":
            score += scissors + win

    elif opponent == "C":
        if you == "X":
            score += paper + lose
        elif you == "Y":
            score += scissors + draw
        elif you == "Z":
            score += rock + win

    return score


# ______________________MAIN______________________
def main():
    FILE = open("D2.txt").read().strip().splitlines()
    moves = getMoveList(FILE)

    total = 0
    for move in moves:
        total += outcomes(move[0], move[1])

    print(total)


if __name__ == "__main__":
    main()
