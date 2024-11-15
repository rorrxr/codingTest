P = input().split()  # 전화번호 리스트 P
T = input()  # 전화번호 N 접두사

# 카운트 할 변수
cnt = 0

# P의 길이만큼 for문
for i in range(len(P)):
    # 현재 인덱스가 T와 같다면
    if P[i] == T:
        # 건너뛰기
        continue
    # 다르면
    else:
        # 현재 인덱스가 포함되는지 확인
        if P[i][:len(T)] == T:
            # 포함된다면 cnt를 증가시김
            cnt += 1

# cnt의 개수 출력
print(cnt)  
