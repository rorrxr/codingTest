while(True):
    S =input()

    stack=[] # 괄호를 추가할 stack 리스트 
    
    # "." 이 들어오면 종료
    if S == '.': 
        break

    for w in S:
        # 여는 괄호가 오면 stack에 추가
        if w=='(' or w=='[': 
            stack.append(w)
        
        # ) 인 경우
        if w==')':
            # stack이 비어있지 않고, 마지막 요소가 ( 이면 pop
            if len(stack)!=0 and stack[-1]=='(': 
                stack.pop()
                
            # stack이 비어있거나 짝이 맞지 않으면 stack에 )을 추가하고 break
            else: 
                stack.append(w)
                break
            
        # ] 인 경우
        if w==']': 
            # stack이 비어있지 않고, 마지막 요소가 [ 이면 pop
            if len(stack)!=0 and stack[-1]=='[': 
                stack.pop()
            
            # stack이 비어있거나 짝이 맞지 않으면 stack에 ]을 추가하고 break
            else: 
                stack.append(w)
                break

    # 스택 리스트가 비어있으면 
    if len(stack) == 0:
        # 괄호의 균형이 맞으므로 Yes 출력 
        print('yes')
        
    # 스택 리스트가 비어있지 않으면 
    else: 
        # 괄호의 균형이 맞지 않는 것이므로 No 출력
        print('no')