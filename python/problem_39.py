co = [0]*1001
for a in range(1,334):
    b, c = a, a+1
    while a+b+c < 999:
        b +=1
        s = a**2 + b**2
        while c**2 < s:
            c = c+1
        if c**2 == s:
            co[a+b+c] += 1

print co.index(max(co))
