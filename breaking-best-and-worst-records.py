
def record(array):
    max = array[0]
    min = array[0]
    max_count = 0
    min_count = 0
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
            max_count += 1

        if array[i] < min:
            min = array[i]
            min_count += 1

    return max_count, min_count

print(record([3, 4, 21, 36, 10, 28, 35, 2, 24, 42]))