--Largest prime factor
--
--The prime factors of 13195 are 5, 7, 13 and 29.
--What is the largest prime factor of the number 600851475143 ?

pfac 1 f = f
pfac n f = if mod n f == 0 then pfac (div n f) f else pfac n (f+1)

main = print (pfac 600851475143 2)
