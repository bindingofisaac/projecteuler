"""
10001st prime
"""


def primes(n):
  ps, sieve = [], [True]*(n+1)
  for p in range(2, n+1):
    if sieve[p]:
      ps.append(p)
      for i in range(p*2,n+1,p):
        sieve[i] = False
  return ps

print primes(1000000)[10001-1]
