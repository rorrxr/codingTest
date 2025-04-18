"""
문제
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 

기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 
나와 할아버지는 2촌이 되고, 
아버지 형제들과 할아버지는 1촌, 
나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

입력
사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 
입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 
그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 
넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

출력
입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 
어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

"""

# 입력으로 그래프 표현을 하고
# BFS 사용
# 목표 노드에 도달하면 촌수를 출력하고 도달하지 못하면 -1 출력

# BFS 전체 사람의 수, 촌수를 계산할 출발 노드, 촌수를 계산할 목표 노드, 관계

# --- BFS 함수 ----

# BFS로 계산
# 방문 여부를 기록하기 위해 visited 리스트
# BFS를 사용하기 위해 queue를 초기화(현재 노드, 현재 촌수)

# 큐가 존재할 때까지 while문
# 탐색 중인 노드랑, 현재 노드까지의 촌수를 빼내요

# 목표 노드에 도달하면
    # 현재까지의 촌수를 반환해요

# 현재 노드를 아직 방문을 안 했으면
    # visited를 방문으로 표시
    
    # for문을 사용해서 현재 노드가 모든 근처 이웃 노드까지 바놉ㄱ
        # 이웃 노드가 방문하지 않았다면
            #큐에 (이웃 노드, 현재 촌수 + 1) 추가
    
    # 큐를 모두 탐색하지 못하면 -1 반환


# 입력---
# 전체 사람 수 입력
# 촌수를 계산할 두 사람의 번호를 입력
# 관계의 개수를 입력
# 관계를 튜플로 입력받아서 리스트로 저장

# 결과
# bfs 함수를 호출해서 bfs 전체 사람의 수, 촌수를 계산할 출발 노드, 촌수를 계산할 목표 노드, 튜플 리스트

from collections import deque  # deque를 사용하여 BFS 탐색을 구현
import sys

input = sys.stdin.readline

# 입력 처리
n = int(input())  # 전체 사람 수 입력
start, end = map(int, input().split())  # 촌수를 계산할 두 사람의 번호 입력
m = int(input())  # 관계의 개수 입력
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

#bfs
def bfs(x, y):
    visited = [False]*(n+1)
    queue = deque([x])
    
    while queue:
        person = queue.popleft()

        if person == y:
            return visited[y]
        
        for neighbor in graph[person]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = visited[person] + 1
    return -1

print(bfs(start, end))