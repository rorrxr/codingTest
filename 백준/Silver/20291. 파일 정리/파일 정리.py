N = int(input()) # 파일 개수
 
arr = [] # 파일의 확장자를 저장
dict = {} # 확장자 카운트
 
for i in range(N):
    # . 기준으로 문자열 분리
    file = input().split('.') 
    # arr 배열에 확장자만 저장
    arr.append(file[1])

# 확장자별로 카운트
for i in arr:
    # 확장자가 존재하면
    if dict.get(i):
        # 확장자 개수를 1 증가
        dict[i] += 1
    else:
        # 확장자가 없으면 1로 초기화
        dict[i] = 1
 
# 확장자별 개수를 오름차순으로 정렬
dict = sorted(dict.items())

# 정렬된 확장자와 개수 출력
for i,j in dict:
    print(i,j)