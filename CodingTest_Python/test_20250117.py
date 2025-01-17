# 문제 링크: https://www.acmicpc.net/problem/11663
import sys
input = sys.stdin.read
n, m = map(int, input().split())
points = list(map(int, input().split()))
points.sort()
from bisect import bisect_left, bisect_right
for _ in range(m):
    l, r = map(int, input().split())
    print(bisect_right(points, r) - bisect_left(points, l))