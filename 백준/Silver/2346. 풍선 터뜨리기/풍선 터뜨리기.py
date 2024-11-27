from collections import deque

# 입력 받기
n = int(input())
balloons = list(map(int, input().split()))

# 풍선 번호와 이동 값을 저장할 deque
dq = deque((i + 1, balloons[i]) for i in range(n))

# 결과를 저장할 리스트
result = []

while dq:
    # 현재 풍선 꺼내기
    index, move = dq.popleft()
    result.append(index)
    
    if not dq:  # 더 이상 풍선이 없으면 종료
        break
    
    # 이동 값에 따라 이동하기
    if move > 0:
        # 오른쪽으로 이동할 경우, move - 1 만큼 앞의 풍선들을 뒤로 보낸다
        for _ in range(move - 1):
            dq.append(dq.popleft())
    else:
        # 왼쪽으로 이동할 경우, abs(move) 만큼 뒤의 풍선들을 앞으로 보낸다
        for _ in range(abs(move)):
            dq.appendleft(dq.pop())

# 결과 출력
print(' '.join(map(str, result)))
