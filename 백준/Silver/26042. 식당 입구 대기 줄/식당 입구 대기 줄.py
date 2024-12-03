"""
학생이 학교 식당에 도착하고 식사가 준비되는 n개의 정보가 저장된 A가 주어진다. 
A에 저장된 첫 번째 정보부터 n번째 정보까지 순서대로 처리한 다음, 
식당 입구에 줄을 서서 대기하는 학생 수가 최대가 되었던 순간의 학생 수와 
이때 식당 입구의 맨 뒤에 대기 중인 학생의 번호를 출력하자. 

대기하는 학생 수가 최대인 경우가 여러 번이라면 
맨 뒤에 줄 서 있는 학생의 번호가 가장 작은 경우를 출력하자.

A에 저장된 n개의 정보는 아래 두 가지 유형으로 구분된다. 

첫 번째가 유형 1, 두 번째가 유형 2이다.

1: 
A 학생 번호가 양의 정수 A인 학생 1명이 학교 식당에 도착하여 
식당 입구의 맨 뒤에 줄을 서기 시작한다.

2: 
식사 1인분이 준비되어 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식사를 시작한다.
식사 1인분이 준비될 때는 식당 입구에서 대기 중인 학생이 항상 존재한다. 
식당 입구에 줄을 서서 대기하였으나 식사가 준비 안 된 학생은 식사를 못 한다.
"""

# Keyword : 구현, 자료구조, 큐

import sys
from collections import deque

input = sys.stdin.readline

# N개의 정보 입력
N = int(input())

# 대기 중인 학생들을 저장할 큐
queue = deque()

# 대기 중인 학생 수가 최대가 되었을 때 기록할 값
max_students = [0, 0]

# N개의 정보까지 for문
for _ in range(N):
    # 정보 A 입력
    A = list(map(int, input().split()))  # 입력
    
    # 입력이 2라면
    if A[0] == 2:  
        # 현재 대기줄 맨 앞에 있는 학생을 제거
        queue.popleft()
    else:  
        # 마지막에 줄을 세움
        queue.append(A[1])

    # 현재 대기 중인 학생 수
    current_students = len(queue)

    # 대기 중인 학생 수가 최대인 경우
    if current_students > max_students[0]:
        max_students[0] = current_students
        max_students[1] = queue[-1]  # 맨 뒤 학생 번호
    
    # 대기 중인 학생 수가 최대인 경우     
    elif current_students == max_students[0]:
        # 맨 뒤 학생 번호가 더 작은 값
        max_students[1] = min(max_students[1], queue[-1])

# 출력
print(max_students[0], max_students[1])