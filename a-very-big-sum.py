#Complexity: O(N)

def aVeryBigSum(n, array):
    arr_len = len(array)
    arr_sum = 0
    for i in range(arr_len):
        arr_sum += array[i]
    return arr_sum

arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

print(aVeryBigSum(5, arr))