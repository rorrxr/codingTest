# 문제 링크: https://www.acmicpc.net/problem/1541
import sys
input = sys.stdin.read
expr = input().strip().split('-')
result = sum(map(int, expr[0].split('+')))
for e in expr[1:]:
    result -= sum(map(int, e.split('+')))
print(result)