# 입력받기
n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

# A - B와 B - A 차집합 구하기
a_diff_b = a - b
b_diff_a = b - a

# 대칭 차집합 크기 계산
result = len(a_diff_b) + len(b_diff_a)

# 결과 출력 
print(result)