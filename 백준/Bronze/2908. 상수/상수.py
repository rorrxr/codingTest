# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 
# 예를 들어, 734와 893을 칠판에 적었다면, 
# 상수는 이 수를 437과 398로 읽는다. 
# 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

# 문자열 역순을 하고
# 숫자 1과 숫자 2를 판별한다

a, b = input().split()

# 문자열 역순
a = a[::-1]
b = b[::-1]

if a > b:
    print(a)
if a < b:
    print(b)
