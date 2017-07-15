#Complexity: O(N)

def points(array1, array2):
    n = len(array1)
    alice = 0
    bob = 0
    for i in range(n):
        if array1[i] > array2[i]:
            alice += 1
        elif array1[i] < array2[i]:
            bob += 1
    return alice, bob

array1 = [5, 6, 7]
array2 = [3, 8, 10]

print(points(array1, array2))