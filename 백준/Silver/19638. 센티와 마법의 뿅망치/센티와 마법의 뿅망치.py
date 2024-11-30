import sys, heapq
input = sys.stdin.readline

# 1. 각 데이터 입력받기
n, h, t = map(int, input().split())

# 2. 거인들의 키 heapq 리스트로 저장
giants = [-int(input()) for _ in range(n)]
heapq.heapify(giants)
# 망치질 횟수 저장
cnt = 0

# 3. 망치질 횟수만큼 반복
for i in range(t):
    # 1) 가장 큰 거인이 1명이거나, 센티보다 키가 작을 때 멈춤
    if -giants[0] == 1 or -giants[0] < h:
        break
    else:
        # 그 외에는 peapq에서 제일 큰 값을 /2를 하여 giants에 저장
        heapq.heapreplace(giants, -(-giants[0] // 2))
        # 망치질 횟수 1 증가
        cnt += 1

# 만약 가장 큰 키가 센티보다 크다면?
if -giants[0] >= h:
    print('NO', -giants[0], sep='\n')
    # 그 외는?
else:
    print('YES', cnt, sep='\n')