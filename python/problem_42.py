f = open("/Users/vivek/Downloads/words.txt")
a = "".join(f.read().strip().split("\"")).split(",")
f.close()

t = []
i = 0
while i < 14*26:
    i += 1
    t.append((i*(i+1))/2)

def tw(w):
    s = 0
    for i in w:
        s += ord(i) - 64
    return s
ans = 0
for i in a:
    s = tw(i)
    if s in t: 
        ans = ans+1

print ans
