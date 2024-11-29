N, M = map(int, input().split())
song = {}

for _ in range(N):
    T, S, a1, a2, a3, a4, a5, a6, a7 = input().split()
    # 첫 세 음만 리스트로 저장
    A = [a1, a2, a3]
    # key가 노래 제목 value가 첫 세 음
    song[S] = A		

for _ in range(M):
    B = input().split()
    count = 0	# 같은 노래가 몇 개인지
    title = ""	# 노래 제목

    for s in song:
        # 세 음이 같다면
        if B == song[s]: 
            count += 1
            title = s # title 변수는 count가 1일때만

    if count >= 2:
        print("?")
    elif count == 1:
        print(title)
    else:
        print("!")