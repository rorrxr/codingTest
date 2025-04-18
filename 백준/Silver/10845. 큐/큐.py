from collections import deque
import sys

# 빠른 입력 sys.stdin.readline()을 사용해야 시간초과가 나지 않음
N = int(sys.stdin.readline())

# 덱 선언
d = deque()

# 스택: 맨 앞/뒤에 블록을 추가한 기록
stack = []

for _ in range(N):
    # 빠른 입력 받기
    a = sys.stdin.readline().split()
    
    # 정수 X를 큐에 넣는 연산
    if a[0] == "push":
        d.append(int(a[1]))
    
    # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
    # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력
    if a[0] == "pop":
        if d:
            print(d.popleft())
        else:
            print(-1)
    
    
    # 큐에 들어있는 정수의 개수를 출력
    if a[0] == "size":
        print(len(d))
    
    # 덱이 비어있으면 1을, 아니면 0을 출력
    if a[0] == "empty":
        if not d:        
            print(1)
        else:
            print(0)
    
    # 덱의 가장 앞에 있는 정수를 출력
    # 만약 덱에 들어있는 정수가 없는 경우 -1 출력
    if a[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    
    # 덱의 가장 앞에 있는 정수를 출력
    # 만약 덱에 들어있는 정수가 없는 경우 -1 출력
    if a[0] == "back":
        if d:
            print(d[-1])
        else:
            print(-1)