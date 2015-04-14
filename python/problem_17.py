"""
Number letter counts
"""
from num2words import num2words as n

print sum(map(lambda x: len(''.join(''.join(n(x).split('-')).split(' '))), range(1,1001)))
