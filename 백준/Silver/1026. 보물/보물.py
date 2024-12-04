"""
S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 

단, B에 있는 수는 재배열하면 안 된다.

**S의 최솟값**을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 
둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 
셋째 줄에는 B에 있는 수가 순서대로 주어진다. 

N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 S의 최솟값을 출력한다.
"""

# 풀이

# 최소값을 만들기 위해 배열을 재배열

# A는 B[i]가 클수록 A[i]는 작게 만들어서 
# 그 곱의 합을 최소화하기 위해서 내림차순으로 정렬

# B는 큰 B[i]에 작은A[i]가 곱해져서 
# 최소값을 만들 수 있기 때문에 오름차순으로 정렬

# 따라서
# A는 내림차순으로 정렬
# B는 오름차순으로 정렬
# 인덱스는 0번부터 N-1번까지 곱해주면
# 최소값이 나옴

import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S = 0

# A를 내림차순 정렬
A.sort(reverse=True)

# B를 오름차순 정렬
B.sort()

for i in range(N):

    # S += sorted(A[i], reverse=True) * sorted(B[i])

    # S += min(A) * max(B)
    
    # A.pop(A.index(min(A)))
    # B.pop(B.index(max(B)))
    
    S += A[i] * B[i]

print(S)
