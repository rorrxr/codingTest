import sys
input = sys.stdin.readline

# 단어의 개수
n = int(input())

# 단어 리스트 생성
words = []
for _ in range(n):
    # words 리스트에 저장
    words.append(input().rstrip())

for i in range(n):
    for j in range(i, n):
        # words[i]와 words[j]가 역순으로 일치하는지 검사
        if words[i][::-1] == words[j]:
            # 일치하면 해당 단어의 길이와 중간 문자 출력
            print(len(words[i]), words[i][len(words[i]) // 2])
            # 단어를 찾으면 내부 반복문 탈출
            break
    else:
        # 내부 반복문에서 break되지 않으면 외부 반복문 계속 실행
        continue
    # 내부 반복문에서 break되었으면 바깥쪽 반복문도 종료
    break
