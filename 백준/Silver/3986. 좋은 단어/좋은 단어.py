N = int(input())

# 좋은 단어의 개수를 세기 위한 변수
cnt = 0

for _ in range(N):
    stack = [] # 스택 리스트
    S = list(input()) # 단어 입력
    
    # 주어진 단어에서 한 문자씩 처리
    for i in S:
        # 스택이 비어있으면
        if not len(stack): 
            # 현재 문자를 문자 쌍을 맞추기 위해 스택에 넣음   
            stack.append(i)
        # 스택의 맨 위에 있는 문자와 현재 문자가 같으면
        elif stack[-1] == i:
            # 짝이 맞는 것이므로 스택에서 pop
            stack.pop(-1)
        # 스택의 맨 위에 있는 문자와 현재 문자가 다르면
        else:
            # 짝이 맞지 않으므로 스택에 현재 문자 추가
            stack.append(i)
    
    # 스택이 비어있으면 
    if not len(stack):
        # 모든 문자 쌍이 맞춰졌다는 의미로, 좋은 단어임
        # 따라서 cnt를 1 증가
        cnt += 1

print(cnt)