"""
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1:
8

예제 출력 1:
92
"""

import sys

def n_queens(row):
    """
    백트래킹을 이용해 퀸을 배치하는 함수
    """
    global count
    if row == N:  # 모든 행에 퀸을 배치하면 경우의 수 증가
        count += 1
        return

    for col in range(N):  # 모든 열에 대해 퀸을 배치 시도
        if not col_used[col] and not diag1[row + col] and not diag2[row - col + (N - 1)]:  
            # 현재 위치에 퀸을 놓을 수 있는 경우
            col_used[col] = diag1[row + col] = diag2[row - col + (N - 1)] = True  # 퀸 배치
            n_queens(row + 1)  # 다음 행으로 이동
            col_used[col] = diag1[row + col] = diag2[row - col + (N - 1)] = False  # 백트래킹 (원래대로 복구)

N = int(sys.stdin.readline().strip())  # 입력 받기
col_used = [False] * N  # 열(column) 사용 여부 체크
diag1 = [False] * (2 * N - 1)  # 왼쪽 아래 대각선 체크
diag2 = [False] * (2 * N - 1)  # 오른쪽 아래 대각선 체크
count = 0  # 가능한 경우의 수 저장 변수

n_queens(0)  # 첫 번째 행부터 시작
print(count)  # 퀸을 놓는 방법의 수 출력

