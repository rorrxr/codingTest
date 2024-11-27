def parenthesis_verification(s):
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    
    return len(stack) == 0
    
    

n = int(input()) # 테스트 케이스의 수
results = []

for i in range(n):
    target = input()
    results.append("YES" if parenthesis_verification(target) else "NO")

for result in results:
    print(result)