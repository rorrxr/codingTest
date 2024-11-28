from collections import deque

N = int(input())

for i in range(1, N+1):
    str = input()
    w = str.split()
    
    stack = []  # 빈 스택 생성
    for word in w:
        stack.append(word)  # 스택에 단어 넣기
    
    reverse = ''
    
    while stack:
        reverse += stack.pop() + " "  # 스택에서 단어를 뒤집어서 꺼내기
        
    # 출력
    print(f"Case #{i}: {reverse.strip()}")