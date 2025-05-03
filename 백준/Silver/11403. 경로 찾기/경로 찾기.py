import sys
from typing import List

def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    # 모든 정점 쌍에 대해 중간 정점 k를 거쳐가는 경로 확인
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # i -> k 경로와 k -> j 경로가 모두 존재하면 i -> j 경로도 존재함
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    return graph

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    
    # 인접 행렬 입력 받기
    graph = [list(map(int, input().split())) for _ in range(n)]

    # 경로 존재 여부를 플로이드-워셜로 계산
    result = floyd_warshall(graph)

    # 결과 출력
    for row in result:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()