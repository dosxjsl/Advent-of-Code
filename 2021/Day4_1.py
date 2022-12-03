# ______________________FUNCTIONS______________________

# ______________________MAIN______________________


def main():
    file = open("Day4.txt").read().strip().split(",")
    file = [int(i) for i in file]
    # print(file)

    for i in range(80):
        for j in range(len(file)):
            if file[j] == 0:
                file.append(8)
                file[j] = 6
            else:
                file[j] -= 1

        # print(file)
    print(len(file))


if __name__ == "__main__":
    main()
