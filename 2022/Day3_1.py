import re
import math

# ______________________FUNCTIONS______________________

# ______________________MAIN______________________
def main():
    FILE = open("D3.txt").read().strip().splitlines()
    alphabet = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))
    same = []
    total = 0

    for line in FILE:
        firstHalf = line[: len(line) // 2]
        secondHalf = line[len(line) // 2 :]
        common = list(set(firstHalf).intersection(secondHalf))

        # print(alphabet.index(common[0]))
        total += alphabet.index(common[0]) + 1

        same.extend(common)

    print(total)


if __name__ == "__main__":
    main()
