def func(n, start, end):
  # 가장 작은 네모의 한 점 설정
  if n == 1:
      arr[start][start] = 1

  else:
      for i in range(start, end+1): # 세로 방향
          for j in range(start, end+1): # 가로 방향
              # i(가로)가 첫 번째 혹은 마지막일 경우
              if i == start or i == end:
                 # 외곽선에 별을 찍는다
                  arr[i][j] = 1
              else:
                  # j(세로)가 첫 번쨰 혹은 마지막 경우
                  if j == start or j == end:
                      arr[i][j] = 1
      # 그 후 크기를 줄여서 더 작은 네모를 출력
      # start는 2 증가, end는 2 감소
      func(n-1, start+2, end-2)

# 정수 입력
n = int(input())
# 사각형의 크기 계산
x = 4 * (n-1) + 1

# 이차원 배열
arr = [[0] * x for _ in range(x)]

# 함수 실행
func(n, 0, 4*(n-1))

# 출력
for i in range(x):
  for j in range(x):
      if arr[i][j]: # 별 출력
          print('*', end='')
      else: # 공백 출
          print(' ', end='')
  print()