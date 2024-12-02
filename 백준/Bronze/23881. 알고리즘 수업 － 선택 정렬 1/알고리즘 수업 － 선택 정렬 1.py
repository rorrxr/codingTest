def selection_sort(arr, k):
    n = len(arr)
    count = 0

    for last in range(n-1, 0, -1):
        i = last
        for j in range(0, last):
            if arr[j] > arr[i]:
                i = j

        if i != last:
            arr[last], arr[i] = arr[i], arr[last]
            count += 1

            if count == k:
                print(arr[i], arr[last])
                return

    print(-1)

# 입력 처리
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 선택 정렬 수행 및 결과 출력
selection_sort(arr, k)