import re

# ______________________FUNCTIONS______________________
def solve1(input):
    total = 0
    for line in input:
        line = [int(i) for i in re.sub(r"[-,]", " ", line).split(" ")]

        arr1 = list(range(line[0], line[1] + 1))
        arr2 = list(range(line[2], line[3] + 1))

        if len(arr1) <= len(arr2):
            # if all in ARR1 are in ARR2
            if all(item in arr2 for item in arr1):
                total += 1
        else:
            # If all in ARR2 are in ARR1
            if all(item in arr1 for item in arr2):
                total += 1
    print(total)


def solve2(input):
    overlaps = 0
    for line in input:
        line = [int(i) for i in re.sub(r"[-,]", " ", line).split(" ")]

        arr1 = list(range(line[0], line[1] + 1))
        arr2 = list(range(line[2], line[3] + 1))
        if len(list(set(arr1) & set(arr2))) > 0:
            overlaps += 1

    print(overlaps)


# ______________________MAIN______________________
def main():
    FILE = open("D4.txt").read().strip().splitlines()
    solve1(FILE)
    solve2(FILE)


if __name__ == "__main__":
    main()
