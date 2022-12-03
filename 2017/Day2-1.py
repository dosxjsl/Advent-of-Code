file = open("D2.txt")
data = file.read().splitlines()
total = 0


def bigNsmall(array):
    max = array[0]
    min = array[0]

    # for i in range(len(array) - 1):
    #     if array[i + 1] > max:
    #         max = array[i + 1]
    #     if array[i + 1] < min:
    #         min = array[i + 1]
    array.sort()
    min = array[0]
    max = array[len(array) - 1]
    return min, max


for i in range(len(data)):
    arr = data[i].split()
    for j in range(len(arr)):
        arr[j] = int(arr[j])
    nums = bigNsmall(arr)
    total = total + (nums[1] - nums[0])

print(total)
