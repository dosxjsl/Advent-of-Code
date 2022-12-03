import re
import math

# ______________________FUNCTIONS______________________

# aa bb cc dd ee
# aa bb cc dd aa
# aa bb cc dd aaa

# ______________________MAIN______________________
def main():
    file = open("D4.txt").read().strip().splitlines()
    passwords = 0
    for code in file:
        code = code.split()
        duplicates = len(list(set([word for word in code if code.count(word) > 1])))
        if duplicates == 0:
            passwords += 1

    print(passwords)


if __name__ == "__main__":
    main()
