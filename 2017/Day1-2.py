import re
import math

# ______________________FUNCTIONS______________________
# ______________________MAIN______________________
def main():
    file = open("D1.txt").read().strip()
    file = [int(i) for i in list(file)]

    sum = 0
    halfway = int(len(file) / 2)

    for i in range(len(file) - halfway):
        print(file[i], file[i + halfway])
        if file[i] == file[i + halfway]:
            sum += file[i]
    # if file[0] == file[-1]:
    #     sum += file[0]

    print(sum * 2)


if __name__ == "__main__":
    main()
