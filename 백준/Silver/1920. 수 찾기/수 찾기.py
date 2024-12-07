def binary_search(arr, target):
    """
    이진 탐색 함수.
    정렬된 리스트 `arr`에서 `target`을 탐색합니다.
    """
    left, right = 0, len(arr) - 1  # 탐색 범위를 리스트 전체로 초기화

    while left <= right:  # 탐색 범위가 유효한 동안 반복
        mid = (left + right) // 2  # 중간 인덱스 계산
        if arr[mid] == target:  # 중간 값이 타겟과 같으면 찾음
            return True
        elif arr[mid] < target:  # 타겟이 중간 값보다 크면 오른쪽 탐색
            left = mid + 1
        else:  # 타겟이 중간 값보다 작으면 왼쪽 탐색
            right = mid - 1
    return False  # 탐색 범위를 모두 확인했지만 타겟을 찾지 못한 경우

# 입력 처리
N = int(input().strip())  # 첫 번째 줄: 정수 N (리스트 A의 크기)
A = list(map(int, input().strip().split()))  # 두 번째 줄: N개의 정수로 이루어진 리스트 A
M = int(input().strip())  # 세 번째 줄: 정수 M (쿼리의 개수)
queries = list(map(int, input().strip().split()))  # 네 번째 줄: M개의 정수로 이루어진 쿼리 리스트

# 정렬
A.sort()  # 이진 탐색을 위해 리스트 A를 오름차순으로 정렬

# 이진 탐색을 통한 결과 계산
results = []
for query in queries:  # 각 쿼리 값에 대해
    if binary_search(A, query):  # A 리스트에서 쿼리 값을 이진 탐색
        results.append(1)  # 찾은 경우 1을 추가
    else:
        results.append(0)  # 찾지 못한 경우 0을 추가

# 결과 출력
for result in results:  # 각 쿼리 결과를 순서대로 출력
    print(result)
