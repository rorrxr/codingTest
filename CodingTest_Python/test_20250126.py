# 문제 링크: https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.read
stack = []
data = input().split('\n')
for cmd in data[1:]:
    if cmd.startswith("push"):
        _, num = cmd.split()
        stack.append(num)
    elif cmd == "pop":
        print(stack.pop() if stack else -1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(1 if not stack else 0)
    elif cmd == "top":
        print(stack[-1] if stack else -1)