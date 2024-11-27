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
    
    # 버튼 1: 맨 뒤에 블록 추가
    if a[0] == '1':
        d.append(a[1])  # 덱의 맨 뒤에 블록 추가
        stack.append(False)  # 뒤에 추가된 블록임을 기록
    
    # 버튼 2: 맨 앞에 블록 추가
    if a[0] == '2':
        d.appendleft(a[1])  # 덱의 맨 앞에 블록 추가
        stack.append(True)  # 앞에 추가된 블록임을 기록
        
        # 버튼 3: 가장 나중에 추가된 블록 제거
    if a[0] == '3':
        if d:  # 덱이 비어있지 않으면
            # stack에서 가장 최근에 추가된 블록의 위치를 확인
            if stack.pop():  # 앞에 추가된 블록이었으면
                d.popleft()  # 덱의 맨 앞에서 블록 제거
            else:  # 뒤에 추가된 블록이었으면
                d.pop()  # 덱의 맨 뒤에서 블록 제거
        else:
            continue  # 덱이 비어있으면 아무 작업도 하지 않음

# 결과 출력
if len(d) == 0:
    print(0)
else:
    print(''.join(d))  # 덱에 저장된 문자를 이어서 출력
