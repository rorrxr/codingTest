"""
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1:
7
1 6
6 3
3 5
4 1
2 4
4 7

예제 출력 1:
4
6
1
3
1
4

예제 입력 2:
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12

예제 출력 2:
1
1
2
3
3
4
4
5
5
6
6
"""

import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline  # 빠른 입력 사용

n = int(input())  # 노드 개수 입력

# 트리 생성 
tree = [[] for _ in range(n+1)]

# 간선 정보 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 부모 노드를 저장할 리스트
parents = [0] * (n+1)  # 부모 정보 저장 

def dfs(node, parent):
    parents[node] = parent  # 현재 노드의 부모 기록
    for child in tree[node]:  # 현재 노드와 연결된 자식 노드 탐색
        if child != parent:  # 방문하지 않은 노드만 탐색
            dfs(child, node)

# DFS 수행
dfs(1, 0)

# 2번 노드부터 N번 노드까지 부모 노드 출력
for i in range(2, n+1):
    print(parents[i])
