"""
그래서 진영 주식회사는, 

다른 모든 지원자와 비교했을 때 

서류심사 성적과 면접시험 성적 중 
적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 

즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 
서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 
**신입사원의 최대 인원수**를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 
각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 

둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적,
면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 

두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

출력
각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.

"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    
    # 참가자의 성적을 저장할 리스트
    scores = []
    
    # 참가자의 성적 score 리스트에 저장
    for _ in range(N):
        scores.append(list(map(int, input().split())))
    
    # 선택할 수 있는 사람의 최소 수
    cnt = 1
    
    # 성적 오름차순 정렬
    scores.sort()

    # for j in range(i+1, N):
    #     if scores[i][0] <= scores[j][0] and scores[i][1] <= scores[j][1]:
    #         count += 1
            
    # max_count = max(max_count, count)
    
    # 첫 번째 참가자의 면접 점수를 max에 저장
    max = scores[0][1]

    # 두 번째 사람부터 시작 for문
    for i in range(1,N):
        # 만약 현재 사람의 서류 점수가 이전에 선택한 사람보다 낮으면
        if scores[i][1] < max :
            # cnt 증가
            cnt += 1
            # 선택한 사람의 서류 점수를 max에 저장
            max = scores[i][1]
        
    print(cnt)
