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

    if you == "X":
        rock = 1
        if opponent == "A":
            # rock V rock
            score += rock + draw
        elif opponent == "B":
            # rock V paper
            score += rock + lose
        elif opponent == "C":
            # rock V scissors
            score += rock + win

    elif you == "Y":
        paper = 2
        if opponent == "A":
            # paper V rock
            score += paper + win
        elif opponent == "B":
            # paper V paper
            score += paper + draw
        elif opponent == "C":
            # paper V scissors
            score += paper + lose

    elif you == "Z":
        scissors = 3
        if opponent == "A":
            # scissors V rock
            score += scissors + lose
        elif opponent == "B":
            # scissors V paper
            score += scissors + win
        elif opponent == "C":
            # scissors V scissors
            score += scissors + draw

    return score


# rock - paper - scissors
# rock - paper - scissors

# ______________________MAIN______________________
def main():
    file = open("D2.txt").read().strip().splitlines()
    moves = getMoveList(file)
    # print(moves)
    total = 0
    for move in moves:
        total += outcomes(move[0], move[1])
    print(total)


if __name__ == "__main__":
    main()
