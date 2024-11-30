import sys, heapq
input = sys.stdin.readline

# 입력 받기
n, h, t = map(int, input().split())

# 거인들의 키를 음수로 변환하여 리스트에 저장 (최대 힙처럼 사용)
giants = [-int(input()) for _ in range(n)]

# giants = []
# for _ in range(n):
#     heapq.heappush(giants, -int(input()))

# 힙으로 변환
heapq.heapify(giants)

cnt = 0

# 마법을 T번까지 사용하거나 거인의 키가 센티보다 작아지면 종료
for i in range(t):
    
    # 현재 가장 큰 거인의 키가 1이거나 센티보다 작은 경우 마법을 멈춤
    if -giants[0] == 1 or -giants[0] < h:
        break
    
    else:
        # 가장 큰 거인의 키를 절반으로 줄이고 다시 힙에 넣기
        heapq.heapreplace(giants, -(-giants[0] // 2))  # 절반으로 줄이기
        cnt += 1

# 마법을 사용하고 나서, 가장 큰 거인의 키가 센티보다 크다면 NO 출력
if -giants[0] >= h:
    print('NO')
    print(-giants[0])
else:
    # 모든 거인의 키가 센티보다 작아지면 YES와 마법 사용 횟수 출력
    print('YES')
    print(cnt)