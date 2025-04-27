N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if n[i - 1] == m[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

lcs_length = dp[N][M]
lcs = []
i, j = N, M
while i > 0 and j > 0:
    if n[i - 1] == m[j - 1]:
        lcs.append(n[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
print(' '.join(map(str, lcs[::-1])))
