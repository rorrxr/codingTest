"""
문제
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.

입력
첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

출력
좋은 수의 개수를 첫 번째 줄에 출력한다.

예제 입력 1:
10
1 2 3 4 5 6 7 8 9 10

예제 출력 1:
8

문제 유형
정렬
이분 탐색
두 포인터
"""

def count_good_numbers(n, nums):
    nums.sort()  # 정렬
    good_count = 0  # 좋은 수 개수
    
    # 각 숫자가 좋은 수인지 판별
    for i in range(n):
        target = nums[i]
        left, right = 0, n - 1  # 투 포인터 초기화
        
        while left < right:
            if left == i:  # 자기 자신 제외
                left += 1
                continue
            if right == i:  # 자기 자신 제외
                right -= 1
                continue

            total = nums[left] + nums[right]

            if total == target:  # 두 수의 합이 타겟과 같으면
                good_count += 1
                break  # 해당 숫자는 좋은 수이므로 다음 숫자로 이동

            elif total < target:  # 합이 작으면 left 증가
                left += 1
            else:  # 합이 크면 right 감소
                right -= 1
    
    return good_count


# 입력 처리
n = int(input())
nums = list(map(int, input().split()))

# 결과 출력
print(count_good_numbers(n, nums))