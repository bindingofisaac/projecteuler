"""
Sum of primes less than 2 million
"""


def primes(n):
  ps, sieve = [], [True]*(n+1)
  for p in range(2, n+1):
    if sieve[p]:
      ps.append(p)
      for i in range(p*2,n+1,p):
        sieve[i] = False
  return ps

print sum([i for i in primes(10000000) if i < 2000000])
