"""
문제
오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

입력
첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. 
(1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

출력
첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. i번째 줄에는 정점 i의 방문 순서를 출력한다. 
시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.

예제 입력 1:
5 5 1
1 4
1 2
2 3
2 4
3 4

예제 출력 1:
1
2
4
3
0

"""

from collections import deque
from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.read
data = input().splitlines()

# 입력 처리
N, M, R = map(int, data[0].split())

# 그래프 생성
graph = defaultdict(list)
for i in range(1, M + 1):
    u, v = map(int, data[i].split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부 및 순서 저장
visited = [0] * (N + 1)
visit_order = [0] * (N + 1)  # 각 정점의 방문 순서를 저장
cnt = 1  # 방문 순서 카운트

def bfs(N, E, R):  # N: 정점 수, E: 간선 집합, R: 시작 정점
    global cnt
    visited = [False] * (N + 1)  # 정점 방문 여부를 N+1 크기로 초기화
    queue = deque([R])  # 큐 생성 및 시작 정점을 추가

    visited[R] = True  # 시작 정점 방문 처리
    visit_order[R] = cnt  # 시작 정점 방문 순서 기록

    while queue:
        u = queue.popleft()  # 큐 맨 앞의 요소를 삭제

        for v in sorted(E[u]):  # 정점 u의 인접 정점 집합을 정렬하여 방문
            if not visited[v]:  # 정점 v가 방문되지 않은 경우
                cnt += 1  # 방문 순서 증가
                visited[v] = True  # 정점 v를 방문했다고 표시
                visit_order[v] = cnt  # 정점 v의 방문 순서를 기록
                queue.append(v)  # 큐의 맨 뒤에 정점 v를 추가

# DFS 실행
bfs(N, graph, R)

# 출력
for i in range(1, N + 1):
    print(visit_order[i])