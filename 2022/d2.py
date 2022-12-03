# with open("test.txt") as f:
#     strat = [(ord(x[0]) - ord("A"), ord(x[2]) - ord("X")) for x in f]
#     print(strat)

# d1 = {0: [1, 2, 0], 1: [0, 1, 2], 2: [2, 0, 1]}
# print(sum(1 + b + 3 * d1[a][b] for a, b in strat))

# d2 = {0: [2, 0, 1], 1: [0, 1, 2], 2: [1, 2, 0]}
# print(sum(3 * b + 1 + d2[a][b] for a, b in strat))

f = open("test.txt", "r")
DATA = [move.strip().replace(" ", "") for move in f.readlines()]
print(DATA)
STRAT_GUIDE_1 = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6,
}
STRAT_GUIDE_2 = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7,
}
print(sum([STRAT_GUIDE_1[pair] for pair in DATA]))
print(sum([STRAT_GUIDE_2[pair] for pair in DATA]))
