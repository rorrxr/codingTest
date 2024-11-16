N = int(input())
list = list(map(int,input().split()))

# 새로운 리스트 생성
l= []

# 입력된 N까지 반복
for i in range(N):
    # 리스트의 번호의 자리에 순서대로 저장
    l.insert(list[i],i+1)

# 리스트를 거꾸로 출력
print(*l[::-1])
