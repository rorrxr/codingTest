import sys
input = sys.stdin.readline

def counting_sort(N):
    # 범위가 1부터 10000까지이므로 10001 크기의 리스트로 초기화(메모리가 더 적다)
    count = [0] * 10001

    # 입력 받은 숫자들의 개수 세기
    for number in range(N):
        input_num = int(input())
        count[input_num] += 1 

    # 정렬된 숫자들 출력
    for i in range(10001):
        if count[i] != 0:
            for _ in range(count[i]):
                print(i)

N = int(input())
counting_sort(N)