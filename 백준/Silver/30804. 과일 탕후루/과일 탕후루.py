"""
문제
은하는 긴 막대에 
$N$개의 과일이 꽂혀있는 과일 탕후루를 만들었습니다. 과일의 각 종류에는 
$1$부터 
$9$까지의 번호가 붙어있고, 앞쪽부터 차례로 
$S_1, S_2, \cdots, S_N$번 과일이 꽂혀있습니다. 과일 탕후루를 다 만든 은하가 주문을 다시 확인해보니 과일을 두 종류 이하로 사용해달라는 요청이 있었습니다.

탕후루를 다시 만들 시간이 없었던 은하는, 막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 했습니다. 앞에서 
$a$개, 뒤에서 
$b$개의 과일을 빼면 
$S_{a+1}, S_{a+2}, \cdots, S_{N-b-1}, S_{N-b}$번 과일, 총 
$N-(a+b)$개가 꽂혀있는 탕후루가 됩니다. 
$(0 \le a, b;$ 
$a+b < N)$ 

이렇게 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 구하세요.

입력
첫 줄에 과일의 개수 
$N$이 주어집니다. 
$(1 \le N \le 200\,000)$ 

둘째 줄에 탕후루에 꽂힌 과일을 의미하는 
$N$개의 정수 
$S_1, \cdots, S_N$이 공백으로 구분되어 주어집니다. 
$(1 \le S_i \le 9)$ 

출력
문제의 방법대로 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 첫째 줄에 출력하세요.

예제 입력 1:
5
5 1 1 2 1

예제 출력 1:
4

예제 입력 2:
3
1 1 1

예제 출력 2:
3

예제 입력 3:
9
1 2 3 4 5 6 7 8 9

예제 출력 3:
2
"""

import sys
from collections import defaultdict
from typing import List

def solution(n: int, fruits: List[int]) -> int:
    count = defaultdict(int)  # 과일 종류별 개수 저장
    left = 0
    max_len = 0

    for right in range(n):
        count[fruits[right]] += 1  # 오른쪽 과일 추가

        # 과일 종류가 3개 이상이면 왼쪽을 줄여서 2종류로 만들기
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]  # 개수가 0이 되면 종류 제거
            left += 1

        # 현재 구간의 길이 갱신
        max_len = max(max_len, right - left + 1)

    return max_len

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    fruits = list(map(int, input().split()))
    print(solution(n, fruits))
