"""
Special Pythagorean tripleto
"""

print [(i,j,k,i*j*k) for i in range(1000) for j in range(1000-i) for k in range(1000-j) if i*i + j*j == k*k and i+j+k == 1000]
