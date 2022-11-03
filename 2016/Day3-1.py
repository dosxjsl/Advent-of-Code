file = open("D3.txt")
data = file.read().strip().splitlines()

possibleTriangles = 0


def sides(side1, side2, side3):
    return (side1 + side2 > side3) & (side2 + side3 > side1) & (side1 + side3 > side2)


for i in range(len(data)):

    newArr = data[i].split()

    if sides(
        int(newArr[0]),
        int(newArr[1]),
        int(newArr[2]),
    ):
        possibleTriangles += 1

print(possibleTriangles)
