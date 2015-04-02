--Largest palindrome product
--
--A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.
--Find the largest palindrome made from the product of two 3-digit numbers.

g x (n:ns) = (if show (x*n) == reverse(show(x*n)) then x*n else 0):(g x ns)
g _ [] = []

f (x:xs)   = (g x [100..999]):(f xs)
f [] = []

main = print (maximum(concat (f [100..999])))
