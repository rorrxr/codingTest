import sys

# 막대기 개수 입력
input = sys.stdin.readline

N = int(input())

# 스택 초기화
stack = []

# 스택에 막대기 추가
for _ in range(N):
    stack.append(int(input()))

# 맨 마지막 막대기 높이
h = stack[-1]

# 카운트를 1로 초기화
cnt = 1

# 스택에서 오른쪽 끝부터 왼쪽 끝까지 역순으로 탐색
for i in reversed(range(N)):
    # 현재 막대기 높이가 l보다 크면 보이는 막대기이므로 
    if stack[i] > h:
        # 카운트를 증가시키고
        cnt += 1
        # h을 현재 막대기로 업데이트
        h = stack[i]

print(cnt)