# 입력받기
a, b, c = map(int, input().split())

# 세 수를 리스트에 넣고 정렬
numbers = [a, b, c]
sorted_numbers = sorted(numbers)

# 정렬된 숫자 출력
print(sorted_numbers[0], sorted_numbers[1], sorted_numbers[2])
