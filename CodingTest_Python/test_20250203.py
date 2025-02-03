# 문제 링크: https://www.acmicpc.net/problem/10610
import sys
input = sys.stdin.read
n = input().strip()
if '0' in n and sum(map(int, n)) % 3 == 0:
    print("".join(sorted(n, reverse=True)))
else:
    print(-1)
