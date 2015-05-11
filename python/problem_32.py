"""
pandigital
"""

def pd(a,b):
    s = str(a) + str(b) + str(a*b)
    if len(s) > 9: return False
    else:
        c = 0
        for i in list("123456789"):
            if i in s:
                c = c + 1
        if c != 9: return False
        else:
            return True

summ = []
for i in range(100):
    for j in range(10000):
        if pd(i,j):
            summ.append(i*j)

print sum(set(summ))
