# 문제 링크: https://www.acmicpc.net/problem/2705
def count_palindrome_partitions(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i, n+1):
            dp[j] += dp[j-i]
    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(count_palindrome_partitions(n))