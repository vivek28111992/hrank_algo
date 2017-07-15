#Complexity: O(N)

def array_sum(array):
    n = len(array)
    sum = 0
    for i in range(n):
        sum += array[i]
    return sum

array = [1, 2, 3, 4, 10, 11]
array_sum(array)
print(array_sum(array))