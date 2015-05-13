s = 0
palins = [i for i in range(1, 1000000) if str(i) == str(i)[::-1]]
for i in palins:
    sb = bin(i)[2:]
    if sb == sb[::-1]:
        s = s+i
print s
