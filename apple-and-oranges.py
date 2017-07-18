#Complexity: O(N)
def distance(s, t, a, b, m, n, apple, orange):
    print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))


distance(7, 11, 5, 15, 3, 2, [-2, 2, 3], [5, -6])