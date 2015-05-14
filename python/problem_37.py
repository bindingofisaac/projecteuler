import sys
def primes(n):
    ps, sieve = [], [True]*(n+1)
    for p in range(2, n+1):
        if sieve[p]:
            ps.append(p)
            for i in range(p*2,n+1,p):
                sieve[i] = False
    return ps

p = primes(1000000)
d = {}
d[1]= filter(lambda x: len(str(x)) == 1, p)
d[2]= filter(lambda x: len(str(x)) == 2, p)
d[3]= filter(lambda x: len(str(x)) == 3, p)
d[4]= filter(lambda x: len(str(x)) == 4, p)
d[5]= filter(lambda x: len(str(x)) == 5, p)
d[6]= filter(lambda x: len(str(x)) == 6, p)

for i in d:
    print len(d[i])

def tp(n):
    sn = str(n)
    li = []
    for i in range(len(sn)):
        li.append(sn[:i])
        li.append(sn[i:])
    li = filter(lambda x: x!='', li)
    return map(lambda x: int(x), li)

"""
d = 0
ans = []
for k in range(len(p)):
    i = p[k]
    c = 0
    lt= tp(i)
    for j in lt:
        if j in p: c = c+1
    if c == len(lt):
        d = d + 1
        if i not in [2,3,5,7]: ans.append(i)
    if d == 15: break
    sys.stdout.write(str(k)+" "+str((float(k)/len(p))*100)+"%\r")
    sys.stdout.flush()

print sum(ans)
"""
