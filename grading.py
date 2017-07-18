
def grading(n, array):
    for i in range(len(array)):
        grades = array[i]
        array[i] = ((grades + 5) - (grades % 5) if (grades % 5) > 2 and grades > 37 else grades)
    return array


print(grading(4, [73, 67, 38, 33]))