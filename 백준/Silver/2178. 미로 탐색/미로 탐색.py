"""
미로는 N x M 크기의 2차원 리스트로 주어지며, 각 위치는 0(벽) 또는 1(길)로 표현됩니다. 
출발지점부터 도착지점까지 이동할 수 있는 경우, BFS를 통해 최단 거리를 반환합니다. 
이동 가능한 경로는 상하좌우로만 가능합니다.
"""
from collections import deque

def bfs(maze, N, M):
    # 방향 벡터 (상, 하, 좌, 우) - 각 좌표 변화량 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS를 위한 큐 초기화, 시작 지점 (0, 0)을 큐에 추가
    queue = deque([(0, 0)])
    
    # 방문 체크를 위한 배열 초기화
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True  # 시작 지점 방문 처리
    
    # BFS 탐색 시작
    while queue:
        # 큐에서 현재 위치를 꺼냄
        x, y = queue.popleft()
        
        # 상하좌우로 이동 가능한 모든 방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 새로운 좌표 계산
            
            # 미로 범위 내에 있고, 아직 방문하지 않았으며, 이동 가능한 길(1)일 경우
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True  # 방문 처리
                # 이동한 칸의 거리를 현재 칸의 거리 + 1로 갱신
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))  # 새로운 위치를 큐에 추가
    
    # 도착 지점 (N-1, M-1)의 거리 값 반환
    return maze[N-1][M-1]


# 입력 처리
N, M = map(int, input().split())  # 미로 크기 입력 (행, 열)
maze = [list(map(int, input().strip())) for _ in range(N)]  # 미로 정보 입력

# BFS 실행 및 결과 출력
result = bfs(maze, N, M)
print(result)
