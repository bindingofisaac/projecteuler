"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def pfac(n):
    f   = 2
    facs = []

    while n != 1:
        if n%f == 0:
            while n%f == 0: 
                n = n//f
            facs.append(f)
        else: f = f+1

    return facs
print pfac(600851475143)[-1]
