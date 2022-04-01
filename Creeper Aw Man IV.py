# import random
#
# n = 1000
# q = 100000
# grid = [['O' for j in range(n)] for i in range(n)]
# i=1
# grid[6][9] = 'Y'
# c=n*n//2
# while i<c:
#     x,y=random.randint(0,n-1),random.randint(0,n-1)
#     if grid[x][y] == 'O':
#         grid[x][y] = i
#         i += 1
#
# # #############################################################
#
# import sys
# sys.stdin = open('test.txt')
# sys.stdout = open('test.txt','w')
# print(n, q)
# for i in grid:
#     print(' '.join([str(j) for j in i]))
# for i in range(q):
#     print(random.randint(1,c),random.randint(1,c),random.randint(1,1000))
# sys.stdout = open('out.txt','w')

##############################################################

# from math import *
#
# n, q = [int(i) for i in input().split()]
# grid = [input().split() for i in range(n)]
# x, y = [(i, grid[i].index('Y')) for i in range(n) if 'Y' in grid[i]][0]
# damage = {}
# for i in range(n):
#     for j in range(n):
#         try: damage[int(grid[i][j]) - 1] = 1 / sqrt((x - i) ** 2 + (y - j) ** 2)
#         except: pass
# numc = len(damage)
#
# ps = [0]
# for i in range(numc): ps.append(damage[i] + ps[-1])
#
# for i in range(q):
#     d, r, h = [int(i) for i in input().split()]
#     print(['dead', 'alive'][h - ps[-1] + ps[min(d + r, numc)] - ps[min(r, numc)] > 0])


x = int(input())
print([i for i in range(x,x+1000000) for j in range(1,i,2) if i > x and i % 2 == 1 and i%j==0][0])