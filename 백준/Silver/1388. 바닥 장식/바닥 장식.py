"""
문제
형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 
형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 

나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 
기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.

이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 
만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 
두 개는 같은 나무 판자이고, 

두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 
두 개는 같은 나무 판자이다.

기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 방 바닥의 세로 크기N과 가로 크기 M이 주어진다. 
둘째 줄부터 N개의 줄에 M개의 문자가 주어진다. 
이것은 바닥 장식 모양이고, '-‘와 ’|‘로만 이루어져 있다.
N과 M은 50 이하인 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.
"""

# 풀이
# 가로: -를 기준으로 연속된 구간을 찾기
# 세로: |를 기준으로 연속된 구간을 찾기
# 방문 여부 체크: 방문한 위치를 기록하여 중복 계산을 방지

# DFS 또는 BFS 사용하여 특정 위치에서 시작하여
# # 연결된 모든 동일한 타입(- 또는 |)을 방문

# 결과는 탐색을 통해 나무판자의 개수 출력

def count_wood_panels(n, m, floor):
    # 방문 여부를 기록하기 위한 2차원 리스트 (False로 초기화)
    visited = [[False] * m for _ in range(n)]
    count = 0  # 나무판자의 개수를 셀 변수

    # 가로 탐색
    for i in range(n):  # 행 탐색
        for j in range(m):  # 열 탐색
            # 아직 방문하지 않았고 현재 위치가 '-'라면 
            if not visited[i][j] and floor[i][j] == '-':
                # 새로운 가로 나무판자 발견
                count += 1  # 나무판자 개수 증가
                k = j  # 현재 열부터 시작
                
                # 현재 행에서 연속된 '-'를 
                while k < m and floor[i][k] == '-':
                    # 모두 방문 True 처리
                    visited[i][k] = True
                    k += 1  # 오른쪽으로 이동

    # 세로 방향 탐색
    for i in range(n):  # 행 탐색
        for j in range(m):  # 열 탐색
            # 아직 방문하지 않았고 현재 위치가 '|'라면 
            if not visited[i][j] and floor[i][j] == '|':
                # 새로운 세로 나무판자 발견
                count += 1  # 나무판자 개수 증가
                k = i  # 현재 행부터 시작
                
                # 현재 열에서 연속된 '|'를 
                while k < n and floor[k][j] == '|':
                    # 모두 방문 True 처리
                    visited[k][j] = True
                    k += 1  # 아래쪽으로 이동

    return count  # 나무판자의 총 개수를 반환

# 입력 처리
n, m = map(int, input().split())  # n: 행의 수, m: 열의 수
floor = [input().strip() for _ in range(n)]  # 바닥 장식 정보 입력 받기 (n개의 문자열)

# 결과 출력
print(count_wood_panels(n, m, floor))  # 나무판자의 개수를 계산하고 출력
