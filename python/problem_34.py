"""
Digit factorials
"""

fact = {0:1}
for i in range(1,10): fact[i] = fact[i-1]*i

def df(n):
    return sum(map(lambda x: fact[int(x)], list(str(n)))) == n

print sum(filter(lambda x: df(int(x)), range(fact[3] , fact[9])))
