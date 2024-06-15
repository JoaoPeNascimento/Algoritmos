n = int(input())
torcedores = list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = torcedores[0]
for i in range(2, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + torcedores[i-1])

print(dp[n], "torcedores podem ser fotografados.")