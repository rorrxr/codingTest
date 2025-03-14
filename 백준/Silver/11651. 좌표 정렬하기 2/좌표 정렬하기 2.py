"""
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

예제 입력 1:
5
0 4
1 2
1 -1
2 2
3 3

예제 출력 1:
1 -1
1 2
2 2
3 3
0 4
"""

import sys

input = sys.stdin.readline

# 점의 개수 입력
N = int(input())

# 점의 리스트 입력받기
points = [list(map(int, input().split())) for _ in range(N)]

# 병합 정렬 구현
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 배열을 절반으로 나누기
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 병합 과정
    merged = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        # 정렬 기준: y값이 작은 순
        # 같다면 x값이 작은 순
        if left_half[i][1] < right_half[j][1] or (left_half[i][1] == right_half[j][1] and left_half[i][0] < right_half[j][0]):
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    # 남은 요소 추가
    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged

# 정렬 실행
sorted_points = merge_sort(points)

# 정렬된 결과 출력
for point in sorted_points:
    print(point[0], point[1])
