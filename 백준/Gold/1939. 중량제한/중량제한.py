"""
문제
N(2 ≤ N ≤ 10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 
물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다. 
그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 
만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, M(1 ≤ M ≤ 100,000)이 주어진다. 
다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1 ≤ A, B ≤ N), C(1 ≤ C ≤ 1,000,000,000)가 주어진다. 

이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다. 
서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다. 

마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다. 
공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.

출력
첫째 줄에 답을 출력한다.
"""

import sys
from collections import deque

# ----------- bfs 함수------------
def bfs(weight):
    # 방문 여부를 기록
    visited = [False] * (N + 1)
    # 시작 노드를 큐에 추가
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()

        # 목표 노드에 도달한 경우 True 반환
        if current == end:
            return True

        # 현재 노드와 연결된 모든 노드 확인
        for next_node, weight_limit in graph[current]:
            # 노드가 방문하지 않았고 다리의 중량 제한이 현재 중량(weight) 이상인 경우
            if not visited[next_node] and weight_limit >= weight:
                visited[next_node] = True
                queue.append(next_node)

    # 목표 노드에 도달하지 못한 경우
    return False

# ----------- 입력 ------------

N, M = map(int, sys.stdin.readline().split())  
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    # A와 B 사이의 중량 제한이 C인 다리 추가
    graph[A].append((B, C))
    graph[B].append((A, C))

start, end = map(int, sys.stdin.readline().split())  # 시작점과 목표점

# -------- 이분 탐색 ------------

# 이분 탐색을 위한 초기값 설정
left = 1  # 중량 제한의 최소값
right = 1000000000  # 중량 제한의 최대값
result = 0  # 가능한 최대 중량 제한

while left <= right:
    mid = (left + right) // 2

    # 현재 중량 제한(mid)에서 두 섬을 연결할 수 있는지 확인
    if bfs(mid):  # 연결 가능
        result = mid  # 가능한 중량 갱신
        left = mid + 1  # 더 큰 중량을 탐색
    else:
        right = mid - 1  # 더 작은 중량을 탐색

# 결과 출력
print(result)