import sys

# 빠른 입력
input = sys.stdin.readline


n = int(input())
arr = []


for _ in range(n):
    arr.append(int(input()))

# 오름차순 정렬
arr.sort()

# 출력
for num in arr:
    print(num)