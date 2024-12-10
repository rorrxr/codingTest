"""
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 

수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

힌트
수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
"""

from collections import deque
import sys

def bfs(N, K):
    # 큐 생성
    queue = deque([(N, 0)])
    
    # visited 초기화
    visited = [False] * 100001
    
    # 시작 위치 방문 표시
    visited[N] = True  
    
    while queue:
        current, time = queue.popleft() # 큐 제거
        
        # 동생의 위치에 도달하면
        if current == K:
            return time
        
        # 현재 위치에서 이동 가능한 다음 위치까지
        for next_step in [current - 1, current + 1, 2 * current]:
            # 이동 가능한 범위 내에서 방문하지 않았다면
            if 0 <= next_step <= 100000 and not visited[next_step]:
                # 다음 위치와 시간을 큐에 추가
                queue.append((next_step, time + 1))
                visited[next_step] = True  # 방문 표시
    
    return -1

input = sys.stdin.readline

N, K = map(int, input().split())
print(bfs(N, K))