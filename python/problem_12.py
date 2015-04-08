"""
Highly divisible triangular number
"""

import math
def nd(n):
    ans = 1
    m = int(math.sqrt(n))
    for i in range(1,m+1):
        if n%i == 0:
            ans = ans + 2
    return ans

i=1
while True:
    j = i*(i+1)//2
    if(nd(j) > 500):
      print j
      break
    i = i+1
