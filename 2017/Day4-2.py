import re
import math

# ___________________FUNCTIONS____________________

# ______________________MAIN______________________
def main():
    file = open("test.txt").read().strip().splitlines()
    passwords = 0

    for code in file:
        code = code.split()
        line_list = [list(item) for item in code]
        for each in line_list:
            # print(each)
            for i in range(len(line_list) - 1):
                print(line_list[i])
                if all(elem in line_list[i + 1] for elem in each):
                    passwords += 1

    print(passwords)


if __name__ == "__main__":
    main()
