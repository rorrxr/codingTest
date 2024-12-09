from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스 수 입력
t = int(input().rstrip())


def bfs(l, startX, startY, endX, endY, matrix):
    # 나이트가 이동할 수 있는 8가지 방향 정의
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    # BFS를 위한 큐 초기화
    q = deque()
    q.append((startX, startY))

    while q:
        # 큐에서 현재 좌표를 꺼냄
        x, y = q.popleft()

        # 목표 좌표에 도달하면 이동 횟수 반환
        if x == endX and y == endY:
            return matrix[x][y] - 1 

        # 나이트가 이동 가능한 8방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 체스판 범위 내 아직 방문하지 않은 위치라면
            if 0 <= nx < l and 0 <= ny < l and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1  # 이동 횟수 추가
                q.append((nx, ny))  # 큐에 추가


# 테스트 케이스 반복
for _ in range(t):
    # 체스판 크기 입력
    l = int(input().rstrip())

    # 시작 위치 입력
    startX, startY = map(int, input().rstrip().split())

    # 목표 위치 입력
    endX, endY = map(int, input().rstrip().split())

    # 체스판 초기화
    matrix = [[0] * l for _ in range(l)]

    # 시작 위치는 1로 설정 (초기값)
    matrix[startX][startY] = 1

    # BFS 실행 결과 출력
    print(bfs(l, startX, startY, endX, endY, matrix))
