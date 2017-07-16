#Complexity: O(N^2)
def staircase(n):

    for i in range(n):
        space = n-i-1
        hashp = n-space
        for j in range(space):
            print(end=" ")
        for k in range(hashp):
            print("#",end="")
        print(end="\n")

staircase(6)