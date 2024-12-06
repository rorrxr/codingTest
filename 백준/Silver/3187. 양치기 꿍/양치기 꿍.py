"""
문제
양치기 꿍은 맨날 늑대가 나타났다고 마을 사람들을 속였지만 이젠 더이상 마을 사람들이 속지 않는다. 
화가 난 꿍은 복수심에 불타 아예 늑대들을 양들이 있는 울타리안에 마구 집어넣어 양들을 잡아먹게 했다.

하지만 양들은 보통 양들이 아니다. 
같은 울타리 영역 안의 양들의 숫자가 늑대의 숫자보다 더 많을 경우 늑대가 전부 잡아먹힌다. 
물론 그 외의 경우는 양이 전부 잡아먹히겠지만 말이다.

꿍은 워낙 똑똑했기 때문에 이들의 결과는 이미 알고있다. 

만약 빈 공간을 '.'(점)으로 나타내고 울타리를 '#', 늑대를 'v', 양을 'k'라고 나타낸다면 
여러분은 몇 마리의 양과 늑대가 살아남을지 계산할 수 있겠는가?

단, 울타리로 막히지 않은 영역에는 양과 늑대가 없으며 양과 늑대는 대각선으로 이동할 수 없다.

입력
입력의 첫 번째 줄에는 각각 영역의 세로와 가로의 길이를 나타내는 
두 개의 정수 R, C (3 ≤ R, C ≤ 250)가 주어진다.

다음 각 R줄에는 C개의 문자가 주어지며 이들은 위에서 설명한 기호들이다.

출력
살아남게 되는 양과 늑대의 수를 각각 순서대로 출력한다.

예제 입력 1:
6 6
...#..
.##v#.
#v.#.#
#.k#.#
.###.#
...###

출력 1:
0 2

입력 2:

8 8
.######.
#..k...#
#.####.#
#.#v.#.#
#.#.k#k#
#k.##..#
#.v..v.#
.######.

출력 2:

3 1

입력 3:
9 12
.###.#####..
#.kk#...#v#.
#..k#.#.#.#.
#..##k#...#.
#.#v#k###.#.
#..#v#....#.
#...v#v####.
.####.#vv.k#
.......####.

출력 3:
3 5
"""

# 한 번 탐색이 시작되면 같은 영역(울타리로 막힌 영역) 내 모든 칸을 방문하여 양과 늑대의 수를 세어야 합니다.

# 탐색이 완료된 영역의 양(k)과 늑대(v) 수를 비교합니다.
# 양이 늑대보다 많으면 늑대는 전부 잡아먹힙니다.
# 그렇지 않으면 양이 전부 잡아먹힙니다.
# 결과에 따라 살아남은 양과 늑대의 수를 기록합니다.

# 지도의 모든 칸을 확인하면서, 방문하지 않은 칸에서 새로운 탐색을 시작합니다.
# 울타리(#)로 구분된 모든 독립된 영역에 대해 탐색을 수행합니다.

# 탐색이 종료되면 최종적으로 살아남은 양과 늑대의 수를 출력합니다.

import sys
from collections import deque

# 입력 처리
input = sys.stdin.read
data = input().splitlines()
R, C = map(int, data[0].split())
grid = [list(data[i + 1]) for i in range(R)]

# 방문 여부 저장
visited = [[False] * C for _ in range(R)]

# 이동 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# def dfs(x, y):
#     global sheep, wolf

#     visited[x][y] = True
    
#     # 현재 위치가 양이라면 카운트 증가
#     if grid[x][y] == 'k':
#         sheep += 1
#     # 현재 위치가 늑대라면 카운트 증가 
#     elif grid[x][y] == 'v':
#         wolf += 1
    
#     # 상하좌우로 이동
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
        
#         # 범위를 벗어나거나 이미 방문했거나 울타리인 경우 스킵
#         # # 새로운 좌표(nx, ny)가 탐색 가능한지 확인
#         # nx < 0 or ny < 0  # 1. 맵의 위쪽 또는 왼쪽 경계를 벗어난 경우
#         # or nx >= R or ny >= C  # 2. 맵의 아래쪽 또는 오른쪽 경계를 벗어난 경우
#         # or visited[nx][ny]  # 3. 이미 방문한 좌표인 경우
#         # or grid[nx][ny] == '#'  # 4. 울타리(#)로 막힌 좌표인 경우
#         if nx < 0 or ny < 0 or nx >= R or ny >= C or visited[nx][ny] or grid[nx][ny] == '#':
#             continue
        
#         # 재귀적으로 DFS 호출
#         dfs(nx, ny)

# BFS 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    sheep, wolf = 0, 0

    # 첫 번째 좌표의 상태 체크
    if grid[x][y] == 'k':
        sheep += 1
    elif grid[x][y] == 'v':
        wolf += 1

    while queue:
        cx, cy = queue.popleft()

        # 상하좌우로 이동
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 범위를 벗어나거나 이미 방문했거나 울타리라면 스킵
            if nx < 0 or ny < 0 or nx >= R or ny >= C or visited[nx][ny] or grid[nx][ny] == '#':
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))

            # 양 또는 늑대인 경우 카운트
            if grid[nx][ny] == 'k':
                sheep += 1
            elif grid[nx][ny] == 'v':
                wolf += 1

    return sheep, wolf

# 결과 저장 변수
total_sheep = 0
total_wolf = 0

# 전체 맵 탐색
for i in range(R):
    for j in range(C):
        if not visited[i][j] and grid[i][j] != '#':  # 방문하지 않았고 울타리가 아닌 경우
            sheep, wolf = bfs(i, j)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

# 결과 출력
print(total_sheep, total_wolf)       