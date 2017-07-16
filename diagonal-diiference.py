#Complexity O(N)

def diagonal_diff(n, arr):
    num_arr = len(arr)
    diagonal_sum1 = 0
    diagonal_sum2 = 0
    for i in range(num_arr):            #loop list for first diagonal
        diagonal_sum1 += arr[i][i]
    b = arr[::-1]                       #reverse list
    for j in range(num_arr):            # loop list for second diagonal
        diagonal_sum2 += b[j][j]
    return abs(diagonal_sum1 - diagonal_sum2)

print(diagonal_diff(3, [[11, 2, 4], [4, 5, 6], [10, 8, -12]]))