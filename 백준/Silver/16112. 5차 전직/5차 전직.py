"""
원래 메이플스토리에서는 한 번에 하나의 아케인스톤만 활성화시켜 놓을 수 있고, 
각각의 아케인스톤에는 최대 5억의 경험치를 채울 수 있습니다. 

그러나 해킹에는 자신이 있었던 메린이 키파는 서버를 해킹해 
아케인스톤의 최대 경험치 제한을 없애 버리고, 
최대 k개의 아케인스톤이 동시에 활성화되어 있을 수 있도록 바꿨습니다. 

따라서 한 퀘스트의 보상 경험치가 여러 개의 아케인스톤에 추가될 수 있습니다. 

예를 들어 1번째와 3번째 아케인스톤이 활성화되어 있는 상태에서 
2번째 퀘스트를 진행해 100,000의 경험치와 2번째 아케인스톤을 획득하면, 
1번째와 3번째 아케인스톤에 각각 100,000의 경험치가 추가되고 

2번째 아케인스톤은 모인 경험치가 0인 상태로 받게 됩니다.

키파는 퀘스트를 원하는 순서대로 진행할 수 있지만, 
같은 퀘스트를 두 번 이상 진행할 수는 없습니다. 

키파는 퀘스트를 진행하면서 아케인스톤을 적절히 활성화 또는 
비활성화시켜서 아케인스톤에 모인 경험치의 합을 최대화하고 싶습니다. 

입력
첫째 줄에 정수 n과 k(1 ≤ k ≤ n ≤ 3 · 105)가 주어집니다.

둘째 줄에 n개의 정수가 공백을 사이에 두고 주어집니다. 
i번째 정수는 ai이며 0보다 크고 108보다 작거나 같습니다.

출력
첫째 줄에 키파가 아케인스톤에 모을 수 있는 경험치의 합의 최댓값을 출력합니다.

예시 입력:
3 2
100 300 200

출력:
800

"""

# Keyword: 그리디 알고리즘, 정렬

import sys
import heapq

input = sys.stdin.readline

# N = 퀘스트의 개수
# K = 동시에 활성화할 수 있는 아케인스톤의 최대 개수

N, K = map(int, input().split())
Q = list(map(int, input().split()))

# k 개의 아케인스톤 경험치 리스트
# exp = []

# 최종 전체 경험치 초기화
total_exp = 0

# cnt 초기화
cnt = 0

# 정렬
Q.sort()

"""
# 큐 생성
# heap = []

# Q.sort(reverse=True)
# for i in range(N):
#     if len(exp) < K:
#         heapq.heappush(exp, i)
#     else:
#         heapq.heappush(exp, i)

# 퀘스트까지 for문 반복
# for i in range(N):
#     if len(heap) < K:
#         # 활성화된 아케인스톤이 K개 이하일 경우
#         # 힙 추가
#         heapq.heappush(heap, Q[i])
#         # 현재 퀘스트의 경험치만큼 total_exp에 추가
#         total_exp += Q[i] * len(heap)
#     else:
#         # K개를 초과하면 
#         # 최소 힙 반환
#         min_exp = heapq.heappop(heap)
#         total_exp -= (Q[i] - min_exp) * len(heap)
#         heapq.heappush(heap, Q[i])
"""


for i in range(N):
    if K > cnt:
        cnt += 1
        total_exp -= Q[i]
    total_exp += Q[i] * cnt    
    
print(total_exp)
