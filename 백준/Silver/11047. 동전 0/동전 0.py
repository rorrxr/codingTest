n, k = map(int, input().split()) # N, K 입력 받기
coins = [int(input()) for _ in range(n)] # 동전 리스트 입력 받기
coins.sort(reverse=True) # 정렬


count = 0 # 필요한 동전 개수
for coin in coins:
    count += k // coin  # 현재 동전으로 만들 수 있는 개수 추가
    k %= coin  # 남은 금액 업데이트
    if k == 0:  # 목표 금액을 만들었으면 종료
        break
print(count)