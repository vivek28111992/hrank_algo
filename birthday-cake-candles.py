#Complexity: O(N)

def candles(n, arr):
    arrlen = len(arr)
    sum = 0
    max = 0
    for i in range(arrlen):
        if arr[i] > max:
            max = arr[i]
            sum = 1
        elif max == arr[i]:
            sum += 1
    return sum

print(candles(4, [3, 2, 1, 3, 3, 5]))