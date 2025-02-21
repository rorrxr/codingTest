"""
문제
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

출력
문제의 조건을 만족하는 쌍의 개수를 출력한다.

예제 입력 1:
9
5 12 7 10 9 1 2 3 11
13

예제 출력 1:
3

"""

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()  # 정렬
left, right = 0, n - 1  # 투 포인터 초기화
count = 0

while left < right:
    current_sum = nums[left] + nums[right]
    
    if current_sum == x:  # 합이 x인 경우
        count += 1
        left += 1
        right -= 1
    elif current_sum < x:  # 합이 x보다 작으면 left 이동
        left += 1
    else:  # 합이 x보다 크면 right 이동
        right -= 1

print(count)