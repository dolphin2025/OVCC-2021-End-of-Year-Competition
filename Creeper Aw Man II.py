#
# import random
# n, h = 1000, 1000000
# grid = [[['O','C'][random.randint(1,1)==1] for j in range (n)] for i in range (n)]
# grid[999][999]='Y'
# import sys
# sys.stdout = open('test.txt','w')
# print(n, h)
# for i in grid:
#     print(''.join(i))

from math import *

n, h = [int(i) for i in input().split()]
grid = [input() for i in range(n)]
x, y = [(i, grid[i].index('Y')) for i in range(n) if 'Y' in grid[i]][0]
damage = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'C':
            damage.append(1 / sqrt((x - i) ** 2 + (y - j) ** 2))
damage.sort()
damage.append(10 ** 10)

for i in range(len(damage)):
    h -= damage[i]
    if h <= 0: break
print(i)
