"""
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.

예제 입력 1:
10

예제 출력 1:
2

예제 입력 2:
3

예제 출력 2:
0
"""

import sys

input = sys.stdin.readline

# N 입력 받기
N = int(input())

# 팩토리얼(N!) 계산 함수
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 끝자리 0의 개수를 세는 함수
def count_zero(n):
    result = 0
    # 끝자리가 0일 때마다 10으로 나누어 0의 개수 카운트
    while n % 10 == 0:
        result += 1
        n //= 10
    return result

# 결과 출력
print(count_zero(factorial(N)))
