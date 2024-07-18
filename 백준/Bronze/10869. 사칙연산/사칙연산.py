# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
a, b = map(int, input().split())

sum = a + b
sub = a - b
mul = a * b
div = a / b
odd = a % b

print(sum)
print(sub)
print(mul)
print(int(div))
print(odd)