# 문제 링크: https://www.acmicpc.net/problem/30445
import sys
input = sys.stdin.read
n, x = map(int, input().split())
numbers = list(map(int, input().split()))
print(1 if x in numbers else 0)