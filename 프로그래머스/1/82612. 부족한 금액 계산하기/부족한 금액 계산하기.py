def solution(price, money, count):

    for i in range(1, count+1):
        money -= (price * i); 
    
    if money < 0:
        answer = abs(money);
    
    else:
        answer = 0;

    return answer