import sys
import heapq

input = sys.stdin.readline

# 입력 받기
n = int(input())

q = []

for _ in range(n):
    num = int(sys.stdin.readline()) 

    # 입력이 0인 경우
    if (num == 0):
        # 큐가 비어있다면 0을 출력
        if len(q) == 0:
            print(0)
        else:
            # 큐에 값이 있다면 최소값을 꺼내서 출력
            print(heapq.heappop(q))
    else:
        # 0이 아닌 숫자라면, 그 숫자를 큐에 삽입
        heapq.heappush(q, num)