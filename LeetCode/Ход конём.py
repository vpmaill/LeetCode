n, m = map(int, input().split())
grid = [[0 for _ in range(55)] for _ in range(55)]
grid[0][0] = 1
for i in range(n):
    for j in range(m):
        grid[i][j] += grid[i - 2][j - 1] + grid[i - 1][j - 2]
print(grid[n - 1][m - 1])
