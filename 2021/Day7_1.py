file = open("test.txt").read().split(",")
file = [int(i) for i in file]
min_pos = 2**31
for i1 in file:
    pos = 0
    for num in file:
        pos += abs(num - i1)
    min_pos = min(min_pos, pos)

print(min_pos)
