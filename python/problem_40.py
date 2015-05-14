s = '0'
for i in range(1,249999):
    s = s + str(i)
f = 1
for i in range(7):
    f = f*int(s[10**i])
print f
