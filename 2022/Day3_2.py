import re
import math
import datetime

# ______________________FUNCTIONS______________________

# ______________________MAIN______________________
def main():
    start = datetime.datetime.now()
    FILE = open("D3.txt").read().strip().splitlines()
    alphabet = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))
    same = []
    total = 0

    for i in range(0, len(FILE), 3):
        a1 = FILE[i]
        a2 = FILE[i + 1]
        a3 = FILE[i + 2]
        common = list((set(a1).intersection(a2)).intersection(a3))

        total += alphabet.index(common[0]) + 1

        same.extend(common)
    end = datetime.datetime.now()
    print(total, end - start)


if __name__ == "__main__":
    main()
