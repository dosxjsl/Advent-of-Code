import re

# ______________________FUNCTIONS______________________
def solve2(moves, stack):
    for line in moves:
        # print(line)
        movements = [int(i) for i in re.findall(r"[0-9]+", line)]

        num = movements[0]
        initial = movements[1] - 1
        final = movements[2] - 1

        letter = stack[initial][-1 * num :]
        stack[final] += letter
        stack[initial] = stack[initial][: (len(stack[initial]) - num)]

        # print(stack)
    word = "".join([x[-1] for x in stack if len(x) != 0])
    print(word)


def solve1(moves, stack):
    for line in moves:

        movements = [int(i) for i in re.findall(r"[0-9]+", line)]

        num = movements[0]
        initial = movements[1] - 1
        final = movements[2] - 1

        for times in range(num):
            letter = stack[initial][-1]
            stack[final] += letter
            stack[initial] = stack[initial][: (len(stack[initial]) - 1)]

        # print(stack)
    word = "".join([x[-1] for x in stack if len(x) != 0])
    print(word)


# ______________________MAIN______________________
def main():
    MOVES = open("D5.txt").read().splitlines()[10:]
    stack = [
        "WRF",
        "THMCDVWP",
        "PMZNL",
        "JCHR",
        "CPGHQTB",
        "GCWLFZ",
        "WVLQZJGC",
        "PNRFWTVC",
        "JWHGRSV",
    ]
    # BLOCKS = open("test.txt").read().splitlines()[0:3]
    solve1(MOVES, stack.copy())  # CVCWCRTVQ
    solve2(MOVES, stack.copy())  # CNSCZWLVT


if __name__ == "__main__":
    main()
