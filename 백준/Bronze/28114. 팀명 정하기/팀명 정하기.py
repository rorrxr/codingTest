"""
성서의 가이드라인에 따르면 팀 이름을 짓는 방법은 두 가지가 있다.

1. 세 참가자의 입학 연도를 100으로 나눈 나머지를 
오름차순으로 정렬해서 이어 붙인 문자열

2. 세 참가자 중 성씨를 영문으로 표기했을 때의 
"첫 글자를 백준 온라인 저지에서 해결한 문제가 많은 사람부터" 
차례대로 나열한 문자열

예를 들어 600문제를 해결한 

18학번 안(AHN)씨, 
2000문제를 해결한 19학번 이(LEE)씨, 
6000문제를 해결한 20학번 오(OH)씨로 구성된 팀을 생각해 보자. 

첫 번째 방법으로 팀명을 만들면 181920이 되고, 
두 번째 방법으로 팀명을 만들면 OLA가 된다.
"""

import sys
input = sys.stdin.readline

Ylist = []
Slist = []

# 문제의 개수 P, 입학 연도 Y, 성씨 S
for i in range(3):
    p, y, s = input().split()
    Ylist.append(int(y))
    Slist.append([int(p), s])  

Ylist.sort()
Slist.sort(reverse=True)

t1 = ""
t2 = ""

for i in range(3):
    # 첫 번째 방법 팀명 출력
    # 입학 연도로 100으로 나눈 나머지 오름차순
    # ex) 181920
    t1 += str(Ylist[i] % 100)
    
    # 두 번째 방법 팀명 출력
    # 성 표기의 첫 글자를 백준 온라인 저지에서 해결한 문제가 많은 사람부터

    t2 += Slist[i][1][0]
    

print(t1)
print(t2)

