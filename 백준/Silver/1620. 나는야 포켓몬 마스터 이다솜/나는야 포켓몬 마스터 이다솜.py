import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# N: 포켓몬 수, M: 문제 수
N, M = map(int, input().split())

# 이름 → 번호 (dict), 번호 → 이름 (list)
pokemon_dict = {}
pokemon_list = [None] * (N + 1)  # 1번부터 시작하므로 인덱스 0은 사용하지 않음

# 도감 데이터 입력
for i in range(1, N + 1):
    name = input().rstrip()
    pokemon_dict[name] = i
    pokemon_list[i] = name

# 문제 풀이
for _ in range(M):
    question = input().rstrip()
    
    if question.isdigit():  # 숫자 입력이면 → 이름 출력
        idx = int(question)
        print(pokemon_list[idx])
    else:  # 이름 입력이면 → 번호 출력
        print(pokemon_dict[question])
