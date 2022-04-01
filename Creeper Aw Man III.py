import sys; sys.setrecursionlimit(10**7)
n = int(input()); grid = [list(input()) for i in range(n)]

def dfs(i, j):
    grid[i][j] = 'O'
    [dfs(i+x,j+y) for x in range(-2,3) for y in range(-2,3) if abs(x)+abs(y)<3 and 0<=x+i<n and 0<=y+j<n and grid[i+x][j+y]=='C']

print(len([dfs(i, j) for i in range(n) for j in range(n) if grid[i][j] == 'C']))
