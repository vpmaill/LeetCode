n, m = map(int, input().split())
N = []
for _ in range(n):
    N.append(list(map(int, input().split())))


def min_weight(a, b):
    dp = [[0] * b for _ in range(a)]
    dp[0][0] = N[0][0]

    for i in range(1, a):
        dp[i][0] = dp[i - 1][0] + N[i][0]

    for j in range(1, b):
        dp[0][j] = dp[0][j - 1] + N[0][j]

    for i in range(1, a):
        for j in range(1, b):
            dp[i][j] = N[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    return dp


grid = min_weight(n, m)
res = ''
a = n - 1
b = m - 1
while a != 0 or b != 0:
    if grid[a][b] - N[a][b] == grid[a - 1][b]:
        res = " D" + res
        a -= 1
    else:
        res = " R" + res
        b -= 1
print(grid[-1][-1], res)
