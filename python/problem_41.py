def primes(n):
    ps, sieve = [], [True]*(n+1)
    for p in range(2, n+1):
        if sieve[p]:
            ps.append(p)
            for i in range(p*2,n+1,p):
                sieve[i] = False
    return ps

p=primes(10000000)

d = {}
d[0] = 0
for i in range(1,10):
    d[i] = filter(lambda x: len(str(x)) == i, p)

def pd(n):
    c = 0
    for i in list("1234567"):
        if i in str(n): c = c+1
    return c == len(str(n))
ans = []
for i in d[7]:
    if pd(i):
        ans.append(i)

print max(ans)
