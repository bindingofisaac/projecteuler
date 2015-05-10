"""
Digit fifth powers
"""
def p(n, e):
    s = list(str(n))
    m = 0
    for i in s:
        m = m + int(i)**e
    if m == n: return True
    else: return False

e = 5
s = 0
for i in range(2,6*9**5):
    if(p(i, e)):
        s = s + i

print s
