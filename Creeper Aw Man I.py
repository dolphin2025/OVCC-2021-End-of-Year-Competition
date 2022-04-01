import random

n = 1000
grid = [[['O', 'C'][random.randint(1, 1) == 2] for j in range(n)] for i in range(n)]
grid[0][0] = 'Y'
grid[1][0] = 'C'

import sys
sys.stdout = open('test.txt', 'w')
print(n)
for i in grid:
    print(''.join(i))

n = int(input())
grid = [input() for i in range(n)]
x, y = [(i, j) for i in range(n) for j in range(n) if grid[i][j]=='Y'][0]
print(['dead', 'alive'][sum(1/((x-i)**2+(y-j)**2)**.5 for i in range(n) for j in range(n) if grid[i][j]=='C')<=20])
print(['dead', 'alive'][sum(1/(abs(x-i)+abs(y-j)) for i in range(n) for j in range(n) if grid[i][j]=='C')<=20])


from math import *

n = int(input())
grid = [input() for i in range (n)]
x, y = [(i, j) for i in range(n) for j in range(n) if grid[i][j]=='Y'][0]
ehearts, mhearts = 20, 20

for i in range (n):
    for j in range (n):
        if grid[i][j] == 'C':
            ehearts -= 1/sqrt((x-i)**2+(y-j)**2)
            mhearts -= 1/(abs(x-i)+abs(y-j))

print(['dead','alive'][ehearts>0])
print(['dead','alive'][mhearts>0])