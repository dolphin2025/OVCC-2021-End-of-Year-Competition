n, h = [int(i) for i in input().split()]
grid = [input() for i in range (n)]
x, y = [(i,grid[i].index('Y')) for i in range (n) if 'Y' in grid[i]][0]
damage = sorted([1]+[1/((x-i)**2+(y-j)**2)**.5 for i in range(n) for j in range(n) if grid[i][j]=='C'])

for i in range(len(damage)):
    h -= damage[i]
    if h<=0: break
print(i)
