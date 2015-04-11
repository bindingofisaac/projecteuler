"""
longest collatz sequence
"""

def c(n):
    ans = 1
    while n!=1:
        if(n%2==0):
            n = n/2
        else:
            n = 3*n+1
        ans = ans+1
    return ans

m = 1
n = 1
for i in range(1, 1000000):
    t = c(i)
    if(t>m):
        m = t
        n = i


print n
