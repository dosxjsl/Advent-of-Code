import re
import math

# ______________________FUNCTIONS______________________


# ______________________MAIN______________________
def main():
    file = open("D1.txt").read().strip()
    file = [int(i) for i in list(file)]

    sum = 0
    for i in range(len(file) - 1):
        if file[i] == file[i + 1]:
            sum += file[i]
    if file[0] == file[-1]:
        sum += file[0]
    print(sum)


if __name__ == "__main__":
    main()
