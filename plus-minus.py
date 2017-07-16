#Complexity O(N)

def plusminus(n, arr):
    zero = 0
    pos = 0
    neg = 0
    for i in range(n):
        if arr[i] == 0:
           zero += 1
        elif arr[i] > 0:
            pos += 1
        else:
            neg += 1

    posDec = ("%.6f" % round(pos/n,6))
    negDec = ("%.6f" % round(neg/n,6))
    zeroDec = ("%.6f" % round(zero/n,6))

    return posDec, negDec, zeroDec

print(plusminus(6, [-4, 3, -9, 0, 4, 1]))