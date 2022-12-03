# ______________________FUNCTIONS______________________
def binaryToDecimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1

    return decimal


def big(input):
    newArr = input.copy()

    for i in range(len(input[0])):
        zeroes = 0
        ones = 0
        zerosPositions = []
        onesPositions = []

        if len(newArr) == 1:
            break

        for index, line in enumerate(newArr):
            if line[i] == "0":
                zeroes += 1
                zerosPositions.append(index)
            elif line[i] == "1":
                ones += 1
                onesPositions.append(index)

        if zeroes > ones:
            for num in onesPositions[::-1]:
                newArr.pop(num)
        else:
            for num in zerosPositions[::-1]:
                newArr.pop(num)

    return "".join(newArr)


def small(input):
    newArr = input.copy()

    for i in range(len(input[0])):
        zeroes = 0
        ones = 0
        zerosPositions = []
        onesPositions = []

        if len(newArr) == 1:
            break

        for index, line in enumerate(newArr):
            if line[i] == "0":
                zeroes += 1
                zerosPositions.append(index)
            elif line[i] == "1":
                ones += 1
                onesPositions.append(index)

        if zeroes <= ones:
            for num in onesPositions[::-1]:
                newArr.pop(num)
        else:
            for num in zerosPositions[::-1]:
                newArr.pop(num)

    return "".join(newArr)


# ______________________MAIN______________________


def main():
    file = open("Day3.txt").read().strip().splitlines()

    oxygen_gen_rating = binaryToDecimal(int(big(file)))

    c02_scubber_rating = binaryToDecimal(int(small(file)))

    life_support_rating = oxygen_gen_rating * c02_scubber_rating
    print(life_support_rating)


if __name__ == "__main__":
    main()
