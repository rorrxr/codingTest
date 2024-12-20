def recursion(s, l, r):
		# 전역변수 global cnt 선언
    global cnt
    # cnt 증가
    cnt += 1
    
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(input())

for i in range(N):
    s = input()
    # cnt 초기화
    cnt = 0
    print(isPalindrome(s), cnt)