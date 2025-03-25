"""
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1:
6 5
1 2
2 5
5 1
3 4
4 6

예제 출력 1:
2

예제 입력 2:
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

예제 출력 2:
1
"""

import sys

# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return parent

input = sys.stdin.readline
n, m = map(int, input().split())  # 정점 수 n, 간선 수 m
parent = [i for i in range(n + 1)]  # 자기 자신을 부모로 초기화
edges = []

# 간선 입력 및 union 연산
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    union_parent(parent, u, v)

# 연결 요소의 개수를 세기 위해 모든 정점의 최종 부모를 찾음
connected_components = set()
for i in range(1, n + 1):
    connected_components.add(find_parent(parent, i))

print(len(connected_components))
