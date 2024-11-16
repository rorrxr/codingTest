# 카드의 개수 입력
N = int(input())

# 할리갈리 카드 딕셔너리
cards = {
    'STRAWBERRY' : 0,
    'BANANA' : 0,
    'LIME' : 0,
    'PLUM' : 0
}

# 카드의 개수만큼 for문 실행
for i in range(N) :
    # 과일의 종류와 과일 개수 입력
    fruit, count = input().split()
    # 과일 개수를 해당 과일 종류 딕셔너리에 더한다
    cards[fruit] += int(count)

# 딕셔너리가 5인 과일이 하나라도 있으면
if 5 in cards.values():
    print('YES') # YES 출력
else: 
    print('NO') # NO 출력