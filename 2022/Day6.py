import re

# ______________________FUNCTIONS______________________
def solve2(input):
    input = list(input)
    for i in range(len(input) - 14):
        fourteen = set([input[j + i] for j in range(14)])
        if len(fourteen) == 14:
            print(i + 14)
            break


def solve1(input):
    input = list(input)
    for i in range(len(input) - 4):
        four = set([input[j + i] for j in range(4)])
        if len(four) == 4:
            print(i + 4)
            break


def part1(input):
    input = list(input)
    for i in range(len(input) - 4):
        four = set([input[j + i] for j in range(4)])
        if len(four) == 4:
            print(i + 4)
            break


# ______________________MAIN______________________
def main():
    MOVES = open("D6.txt").read()

    solve1(MOVES)
    solve2(MOVES)


if __name__ == "__main__":
    main()
