"""
Digit cancelling fractions
"""
from __future__ import division
q = 1
for i in range(10,100):
    for j in range(i,100):
        if len(set(list(str(i))))+len(set(list(str(j))))>len(set(list(str(i)+str(j)))) and (i%10 !=0 or j%10 !=0):
            for x in str(i):
                for y in str(j):
                    if x not in str(j) and y not in str(i) and y != '0':
                        if i/j == int(x)/int(y):
                            q = q*(i/j)

print 1/q
