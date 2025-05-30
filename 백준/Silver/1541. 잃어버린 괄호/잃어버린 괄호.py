"""
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.

예제 입력 1:
55-50+40

예제 출력 1:
-35

예제 입력 2:
10+20+30+40

예제 출력 2:
100

예제 입력 3:
00009-00009

예제 출력 3:
0
"""

import sys

# 빠른 입력 사용
input = sys.stdin.readline

# 앞뒤 공백을 제거
expression = input().strip()

# 결과 값
result = 0
# 숫자
num = ''
# '-' 기호가 등장했는지 여부를 판단하는 변수
minus = False

# 수식을 처음부터 끝까지
for char in expression:
    if char.isdigit():  # 현재 문자가 숫자라면
        num += char  # 숫자를 문자열로 계속 이어 붙임
    else:  # 연산자를 만난 경우
        if minus:  # 이전에 '-'가 등장한 경우, 현재 숫자를 빼야 함
            result -= int(num)
        else:  # 그렇지 않다면 더함
            result += int(num)
        num = ''  # 숫자 초기화

        if char == '-':  # '-' 연산자를 만나면 이후의 숫자들은 모두 빼야 함
            minus = True

# 마지막 숫자를 결과에 반영
if minus:
    result -= int(num)
else:
    result += int(num)

# 최종 결과 출력
print(result)
