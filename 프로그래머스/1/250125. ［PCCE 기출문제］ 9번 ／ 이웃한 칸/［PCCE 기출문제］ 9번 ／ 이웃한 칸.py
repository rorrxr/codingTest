from typing import List, Tuple

def solution(board, h, w):
    n = len(board)  # 보드의 길이
    count = 0  # 같은 색으로 칠해진 칸의 개수
    dh = [0, 1, -1, 0]  # h 좌표 변화량
    dw = [1, 0, 0, -1]  # w 좌표 변화량

    for i in range(4):  # 상하좌우 탐색
        h_check = h + dh[i]  # 체크할 칸의 h 좌표
        w_check = w + dw[i]  # 체크할 칸의 w 좌표

        if 0 <= h_check < n and 0 <= w_check < n:  # 범위 체크
            if board[h][w] == board[h_check][w_check]:  # 같은 색깔인지 확인
                count += 1

    return count