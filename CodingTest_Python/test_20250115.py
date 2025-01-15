# 문제 링크: https://www.acmicpc.net/problem/1406
import sys
input = sys.stdin.read
from collections import deque

data = input().split()  # 여러 줄 입력 처리
s = list(data[0])
stack = deque()

for cmd in data[1:]:
    if cmd == "L" and s:
        stack.appendleft(s.pop())
    elif cmd == "D" and stack:
        s.append(stack.popleft())
    elif cmd == "B" and s:
        s.pop()
    elif cmd.startswith("P"):
        _, x = cmd.split()
        s.append(x)

print("".join(s + list(stack)))