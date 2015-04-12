"""
Lattice Paths

Number of paths from (0,0) to (a,b) -> (20, 20) = (a+b)!/(a!*b!)

"""

def fac(n):
    ans = 1
    for i in range(2, n+1): ans = ans*i
    return ans

print (fac(40))/(fac(20)**2)
