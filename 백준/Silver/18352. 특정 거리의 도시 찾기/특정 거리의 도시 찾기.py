'''
 특정 거리의 도시 찾기
 
 입력 : n, m, k, x -> 첫째 줄에 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호

 의사결정 : 
 
 출력 : x로부터 출발하여, 최단거리가 k인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력. 존재하지 않다면 -1 출력


 ** SUDO CODE ** 

입력
 n : 도시의 개수 (정점)
 m : 도로의 개수 (간선)
 k : 거리 정보 (정점 - 정점)
 x : 출발 도시의 번호 

구현 
인접리스트
bfs 사용
for문에 인덱스에 해당되는 정점 입력받기
visited로 방문 표시

출력 
최단거리가 k인 정점을 오름차순으로 출력
없을 경우 -1 출력
'''
import sys
from collections import deque

n,m,k,x = map(int, sys.stdin.readline().split())
graph =[[] for _ in range(n+1)] 
visited = [False]* (n+1)
result =[0] * (n+1) # 0 1 2 3 4


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def bfs(start_point):
    queue = deque([start_point])
    visited[start_point] =True

    while queue:
        v = queue.popleft()

        for next_city in graph[v]:
            if not visited[next_city]:
                visited[next_city] =True
                result[next_city] = result[v]+1
                queue.append(next_city)

bfs(x)
# 있냐 없냐를
found = False

for i in range(1, n + 1):
    if result[i] == k:
        print(i)
        found = True

if not found:
    print(-1)