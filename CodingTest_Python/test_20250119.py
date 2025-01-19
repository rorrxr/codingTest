# 문제 링크: https://www.acmicpc.net/problem/8595
import sys
import re
input = sys.stdin.read
n = int(input().strip())
s = input().strip()
numbers = map(int, re.findall(r'\d+', s))
print(sum(numbers))