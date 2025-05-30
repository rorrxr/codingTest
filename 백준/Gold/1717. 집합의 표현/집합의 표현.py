"""
문제
초기에 
$n+1$개의 집합 
$\{0\}, \{1\}, \{2\}, \dots , \{n\}$이 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

입력
첫째 줄에 
$n$, 
$m$이 주어진다. 
$m$은 입력으로 주어지는 연산의 개수이다. 다음 
$m$개의 줄에는 각각의 연산이 주어진다. 합집합은 
$0$ 
$a$ 
$b$의 형태로 입력이 주어진다. 이는 
$a$가 포함되어 있는 집합과, 
$b$가 포함되어 있는 집합을 합친다는 의미이다. 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 
$1$ 
$a$ 
$b$의 형태로 입력이 주어진다. 이는 
$a$와 
$b$가 같은 집합에 포함되어 있는지를 확인하는 연산이다.

출력
1로 시작하는 입력에 대해서 
$a$와 
$b$가 같은 집합에 포함되어 있으면 "YES" 또는 "yes"를, 그렇지 않다면 "NO" 또는 "no"를 한 줄에 하나씩 출력한다.

제한
 
$1 ≤ n ≤ 1\,000\,000$ 
 
$1 ≤ m ≤ 100\,000$ 
 
$0 ≤ a, b ≤ n$ 
 
$a$, 
$b$는 정수
 
$a$와 
$b$는 같을 수도 있다.

예제 입력 1:
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

예제 출력 1:
NO
NO
YES
"""

import sys
sys.setrecursionlimit(10**7)  

input = sys.stdin.readline

# 부모를 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

# 두 집합을 합치는 함수
def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        parent[py] = px  # 한 쪽 부모로 합침

# 원소 개수 n, 연산 개수 m 입력
n, m = map(int, input().split())

# 자기 자신이 부모
parent = [i for i in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        # 합집합 연산
        union(a, b)
    else:
        # 같은 집합인지 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
