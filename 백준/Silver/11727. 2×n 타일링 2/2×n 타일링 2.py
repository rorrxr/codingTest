import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (max(3, n + 1))  # 최소 크기 3으로 만들어야 dp[2] 접근 가능

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007

print(dp[n])