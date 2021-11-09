import sys
f = open('008.txt', 'r')
sys.stdin = f

n = int(input())
s = input()
val = 'atcoder'
mod = 10 ** 9 + 7
dp = [[0] * (n + 1) for _ in range(8)]
for i in range(n + 1):
    dp[0][i] = 1
for j in range(len(val)):
    for i, v in enumerate(s):
        if v == val[j]:
            dp[j + 1][i + 1] = (dp[j][i] + dp[j + 1][i]) % mod
        else:
            dp[j + 1][i + 1] = dp[j + 1][i] % mod
print(dp[7][n])