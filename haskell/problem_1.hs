--Multiples of 3 and 5
--
--if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
--Find the sum of all the multiples of 3 or 5 below 1000.

stf (x:xs) = if mod x 3 == 0 || mod x 5 == 0 then x + stf(xs) else stf(xs)
stf [] = 0

main = print (stf [1..999]) 
