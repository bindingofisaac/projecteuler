ans = []

for i in range(1,10000):
    ans.append((i*(3*i-1))/2)

print len(ans)

for i in range(1,10000):
    print i
    for j in range(i+1, 10000):
        pj = j*(3*j-1)
        pk = i*(3*j-1)
        if pj in ans and pk in ans:
            print pk
