n, q = [int(i) for i in input().split()]
grid, ps = [input().split() for i in range(n)], [0]
x, y = [(i, grid[i].index('Y')) for i in range(n) if 'Y' in grid[i]][0]

for _, i, j in sorted([(int(grid[i][j]),i,j) for i in range(n) for j in range(n) if grid[i][j] not in 'OY']):
    ps.append(1 / ((x - i) ** 2 + (y - j) ** 2)**.5 + ps[-1])

for i in range(q):
    d, r, h = [int(i) for i in input().split()]
    print(['dead', 'alive'][h > ps[-1] - ps[min(d + r, len(ps)-1)] + ps[min(r, len(ps)-1)]])
