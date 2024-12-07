"""
1. dfs 함수는 현재 인덱스(index)와 현재까지의 합(current_sum)을 기반으로 탐색합니다.
2. 숫자 리스트의 끝에 도달하면 현재 합이 목표 값과 같은지 확인합니다. 
같으면 1을 반환하고, 그렇지 않으면 0을 반환합니다.
3. 각 숫자에 대해 두 가지 선택을 합니다.
- 해당 숫자를 더한 경우.
- 해당 숫자를 뺀 경우.
4. 모든 경우의 수를 재귀적으로 탐색하여 current_sum이 target과 일치하는 경우를 셉니다.
"""

# 재귀적으로 깊이 우선 탐색을 수행하는 함수
def dfs(numbers, target, index, current_sum):
    # 리스트의 끝에 도달했을 때
    if index == len(numbers):
        # 현재까지의 합이 목표 값과 같으면 1 반환, 아니면 0 반환
        return 1 if current_sum == target else 0
    
    # 현재 숫자를 더한 경우와 뺀 경우를 각각 탐색
    return dfs(numbers, target, index + 1, current_sum + numbers[index]) + \
           dfs(numbers, target, index + 1, current_sum - numbers[index])

# 문제를 해결하는 메인 함수
def solution(numbers, target):
    # DFS 탐색 시작: 인덱스 0부터, 현재 합 0으로 시작
    return dfs(numbers, target, 0, 0)

# 테스트
numbers = [1, 1, 1, 1, 1]  # 숫자 리스트
target = 3  # 목표 값
print(solution(numbers, target))  # 출력: 5
