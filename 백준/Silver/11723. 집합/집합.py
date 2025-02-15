"""
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.
"""

import sys

input = sys.stdin.readline  # 빠른 입력

M = int(input())  # 연산 개수 입력
S = set()  # 집합 S 초기화

for _ in range(M):
    op = input().split()  # 명령어 입력 받기
    if op[0] == 'add':  
        # x를 S에 추가 
        S.add(int(op[1]))
    elif op[0] == 'remove':  
        # x가 S에 존재하면 제거
        S.discard(int(op[1]))  # discard 사용
    elif op[0] == 'check':  
        # x가 S에 존재하면 1, 없으면 0 출력
        print(1 if int(op[1]) in S else 0)
    elif op[0] == 'toggle':  
        # x가 S에 있으면 제거, 없으면 추가
        x = int(op[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif op[0] == 'all':  
        # S를 {1, 2, ..., 20} 으로 변경
        S = set(range(1, 21))
    elif op[0] == 'empty':  
        # S를 공집합으로 변경
        S.clear()