from itertools import permutations as p
def ssd(n):
    c=0
    for i in list("0123456789"):
        if i in str(n): c += 1
    if c == len(str(n)):
        a = str(n)
        l = [2,3,5,7,11,13,17]
        w = 0
        j = 0
        for i in range(1, 8):
            if int(a[i:i+3])%l[j] == 0: w = w+1
            j = j+1
        return w == len(l)

perms = [''.join(i) for i in p("0123456789")]
s = 0
for i in perms:
    if ssd(int(i)):
        s += int(i)

print s
