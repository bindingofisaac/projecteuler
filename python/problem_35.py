from itertools import permutations
import sys

def rotation(n):
    sn = str(n)
    perms = []
    for i in range(len(sn)):
        perms.append(sn[i:]+sn[0:i])
    return map(lambda x: int(x), set(perms))

def primes(n):
    ps, sieve = [], [True]*(n+1)
    for p in range(2, n+1):
        if sieve[p]:
            ps.append(p)
            for i in range(p*2,n+1,p):
                sieve[i] = False
    return ps

p=primes(1000000)
lp = len(p)
d = 0
ans = []
nans = []
for k in range(len(p)):
    i = p[k]
    rs = rotation(i)
    c = 0
    if i in ans : continue
    if i in nans: continue
    for j in rs:
        if j in p: c=c+1
        else: break
    if c == len(rs): 
        ans = ans + rs
        d = d+len(rs)
    else:
        nans = nans + rs
        sys.stdout.write(str(int((float(k)/lp)*100))) 
        sys.stdout.write("%\r");
        sys.stdout.flush()
print ""
print d
