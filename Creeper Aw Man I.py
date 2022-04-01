n = int(input())
grid = [input() for i in range(n)]
x, y = [(i, j) for i in range(n) for j in range(n) if grid[i][j]=='Y'][0]
print(['dead', 'alive'][sum(1/((x-i)**2+(y-j)**2)**.5 for i in range(n) for j in range(n) if grid[i][j]=='C')<=20])
print(['dead', 'alive'][sum(1/(abs(x-i)+abs(y-j)) for i in range(n) for j in range(n) if grid[i][j]=='C')<=20])
