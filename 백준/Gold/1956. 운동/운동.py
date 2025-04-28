import sys

input = sys.stdin.readline

V, E = map(int, input().split())
INF = int(1e9)

# 거리 테이블 초기화
dist = [[INF] * (V + 1) for _ in range(V + 1)]

# 간선 입력
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c

# 플로이드 워셜
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 최소 사이클 찾기
answer = INF
for i in range(1, V + 1):
    if dist[i][i] < answer:
        answer = dist[i][i]

print(answer if answer != INF else -1)
