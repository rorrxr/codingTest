# 딕셔너리 선언
n = {}

def w(a, b, c):
    
    if (a, b, c) in n:
        return n[(a, b, c)]
    else:
        # a, b, c 중 하나라도 0 이하일 경우 1을 반환
        if a <= 0 or b <= 0 or c <= 0:
            n[(a, b, c)] = 1
            return 1
    
        # a, b, c 중 하나라도 20 이상일 경우 w(20, 20, 20)을 반환
        if a > 20 or b > 20 or c > 20:
            n[(a, b, c)] = w(20, 20, 20)
            return n[(a, b, c)]
    
        # a < b < c일 경우
        if a < b and b < c:
            n[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return n[(a, b, c)]

        n[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        
        return n[(a, b, c)]

while True:
    a, b, c = map(int, input().split())

    if(a == -1 and b == -1 and c == -1):
        break


    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")