"""
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1:
6 4
0100
1110
1000
0000
0111
0000

예제 출력 1:
15

예제 입력 2:
4 4
0111
1111
1111
1110

예제 출력 2:
-1
"""

import sys
from collections import deque

input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

# 방문 여부
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

# 상하좌우 방향향
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))  # 시작점, 벽 안 부순 상태
    visited[x][y][0] = 1     # 시작점 방문 처리

    while queue:
        x, y, wall_break = queue.popleft()

        # 도착점에 도달하면 거리 반환
        if x == N - 1 and y == M - 1:
            return visited[x][y][wall_break]

        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 체크
            if 0 <= nx < N and 0 <= ny < M:
                # 이동할 수 있는 곳
                if graph[nx][ny] == 0 and visited[nx][ny][wall_break] == 0:
                    visited[nx][ny][wall_break] = visited[x][y][wall_break] + 1
                    queue.append((nx, ny, wall_break))

                # 벽인데 아직 벽을 안 부순 경우
                if graph[nx][ny] == 1 and wall_break == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][wall_break] + 1
                    queue.append((nx, ny, 1))

    # 도착점에 도달하지 못하면 -1
    return -1

print(bfs(0, 0))
