# 입력받기
input_data = input()

# 입력된 값을 공백을 기준으로 나누기
x, y, w, h = input_data.split()

# 문자열을 정수로 변환
x = int(x)
y = int(y)
w = int(w)
h = int(h)

# 각 경계까지의 거리 계산
distance_to_left = x
distance_to_bottom = y
distance_to_right = w - x
distance_to_top = h - y

# 최솟값 찾기
min_distance = distance_to_left

if distance_to_bottom < min_distance:
    min_distance = distance_to_bottom

if distance_to_right < min_distance:
    min_distance = distance_to_right

if distance_to_top < min_distance:
    min_distance = distance_to_top

# 결과 출력
print(min_distance)