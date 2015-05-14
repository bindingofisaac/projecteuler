def pm(s):
    c =0
    for i in list("123456789"):
        if i in s: c=c+1
    if c == 9: return True
    return False
m=0
for i in range(1000, 10000):
    s = ''
    for j in range(1,3):
       s = s + str(i*j) 
       if len(s) == 9:
           if pm(s):
               if int(s) > m: m = int(s)

print m
