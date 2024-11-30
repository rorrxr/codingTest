import sys
from collections import defaultdict

input = sys.stdin.readline

# 테스트 케이스 수 입력
t = int(input())

for _ in range(t):
    # 의상 종류의 수 n
    n = int(input())
    
    # 의상 종류별로 몇 개의 의상이 있는지 세기
    clothes = defaultdict(int)
    
    for _ in range(n):
        name, kind = input().split()
        clothes[kind] += 1
    
    # 각 의상 종류에 대해 (각각 2가지 선택) -> (입거나 입지 않거나)
    combinations = 1
    for count in clothes.values():
        combinations *= (count + 1)  # 의상 종류마다 입거나 안 입거나 (count + 1)
    
    # 의상 조합에서 아무것도 입지 않는 경우를 제외해야 하므로 1을 빼줌
    print(combinations - 1)
