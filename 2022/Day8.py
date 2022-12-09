import numpy as np


def solve1(input):
    input = np.array(input)
    rows = len(input)
    cols = len(input[0])
    perimeterTrees = 2 * cols + (2 * (rows - 2))

    total = perimeterTrees
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (
                (input[i][j] > max(input[i][:j]))
                or (input[i][j] > max(input[i][j + 1 :]))
                or (input[i][j] > max(input[:i, j]))
                or (input[i][j] > max(input[i + 1 :, j]))
            ):
                total += 1
    print(total)


def solve2(input):
    input = np.array(input)
    rows = len(input)
    cols = len(input[0])

    arr = []
    for i in range(rows):
        for j in range(cols):
            left, right, up, down = 0, 0, 0, 0

            for num in list(reversed(input[i][:j])):
                if input[i][j] > num:
                    left += 1
                else:
                    left += 1
                    break

            for num in input[i][j + 1 :]:
                if input[i][j] > num:
                    right += 1
                else:
                    right += 1
                    break

            for num in list(reversed(input[:i, j])):
                if input[i][j] > num:
                    up += 1
                else:
                    up += 1
                    break

            for num in input[i + 1 :, j]:
                if input[i][j] > num:
                    down += 1
                else:
                    down += 1
                    break

            arr.append(left * right * up * down)

    print(max(arr))


def main():
    FILE = open("./inputs/D8.txt").read().splitlines()

    FILE = [list(line) for line in FILE]
    solve1(FILE)
    solve2(FILE)


if __name__ == "__main__":
    main()
