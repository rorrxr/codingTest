# 몇 번 입력 받을 것인지 출력
N = int(input()) 

for i in range(N):
    I, S = input().split()
    I = int(I)  # 횟수를 정수로 변환

    for j in range(len(S)):
        print(S[j] * I, end='')  # 각 문자를 I번 반복해서 출력, 줄바꿈 없이 이어서 출력
    print()