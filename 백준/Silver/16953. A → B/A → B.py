"""
문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

예제 입력 1:
2 162

예제 출력 1:
5

예제 입력 2:
4 42

예쩨 출력 2:
-1

예제 입력 3:
100 40021

예제 출력 3:
5
"""

import sys
from collections import deque

def bfs(start, end):
    queue = deque([(start, 1)])  # (현재 숫자, 연산 횟수)
    visited = set()  # 중복 탐색 방지용 set

    while queue:
        num, count = queue.popleft()

        if num == end:
            return count  # 연산 횟수 반환

        # 2를 곱하는 연산
        next_num = num * 2
        if next_num <= end and next_num not in visited:
            queue.append((next_num, count + 1))
            visited.add(next_num)

        # 1을 추가하는 연산
        next_num = num * 10 + 1
        if next_num <= end and next_num not in visited:
            queue.append((next_num, count + 1))
            visited.add(next_num)

    return -1  # 만들 수 없는 경우

# 입력 받기
input = sys.stdin.readline().strip().split()
a, b = int(input[0]), int(input[1])

# 결과 출력
print(bfs(a, b))
