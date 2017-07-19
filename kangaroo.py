# Complexity:O(N)
def kangaroo(x1, v1, x2, v2):
    if (x2 > x1 and (v2 > v1 or v1 == v2)) or (x1 == x2 and v2 > v1):
        return "NO"
    else:
        flag = True
        while flag:
            x1 += v1
            x2 += v2
            if x1 == x2:
                flag = False
        return "YES"



print(kangaroo(0, 2, 5, 2))
