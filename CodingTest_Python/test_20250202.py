# 문제 링크: https://www.acmicpc.net/problem/25178
s = input().strip()
print("Yes" if s == s[::-1] else "No")