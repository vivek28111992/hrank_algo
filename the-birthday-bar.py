
def solve(n, s, d, m):
    return len([1 for i in range(n) if sum(s[i:i + m]) == d])

solve(6,[1, 1, 1, 1, 1, 1], 3, 2)