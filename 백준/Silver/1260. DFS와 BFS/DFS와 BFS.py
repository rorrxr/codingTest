"""
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1:
4 5 1
1 2
1 3
1 4
2 4
3 4

예제 출력 1:
1 2 4 3
1 2 3 4

예제 입력 2:
5 5 3
5 4
5 2
1 2
3 4
3 1

예제 출력 2:

3 1 2 5 4
3 1 4 2 5

예제 입력 3:

1000 1 1000
999 1000

예제 출력 3:
1000 999
1000 999
"""

import sys
from collections import deque

# 입력 받기
input = sys.stdin.readline

N, M, V = map(int, input().split())

# 인접 리스트 생성
adj = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 번호가 작은 정점부터 방문하도록 정렬
for i in range(1, N + 1):
    adj[i].sort()

# DFS 구현 (재귀)
def dfs(V):
    visited[V] = True  # 현재 정점 방문 처리
    print(V, end=' ')  # 방문한 정점 출력
    for i in adj[V]:  # 연결된 정점들 탐색
        if not visited[i]:  # 방문하지 않은 경우 탐색 진행
            dfs(i)

# BFS 구현 (큐 사용)
def bfs(V):
    q = deque([V])  # 큐 초기화
    visited[V] = True  # 시작 정점 방문 처리
    while q:
        V = q.popleft()  # 큐에서 정점 꺼내기
        print(V, end=' ')  # 방문한 정점 출력
        for i in adj[V]:  # 연결된 정점들 탐색
            if not visited[i]:  # 방문하지 않은 경우
                q.append(i)  # 큐에 추가
                visited[i] = True  # 방문 처리

# 방문 기록 초기화
visited = [False] * (N + 1)

# DFS 수행
dfs(V)
print()  # 줄바꿈

# 방문 기록 초기화
visited = [False] * (N + 1)

# BFS 수행
bfs(V)
print()

