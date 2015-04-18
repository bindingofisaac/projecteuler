--10001st prime

sieve (p:xs) = p : sieve [x|x <- xs, x `mod` p > 0]
primes = sieve [2..10000000]

main = print(primes !! 10000)
