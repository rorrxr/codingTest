class Edge:
    # 그래프의 간선을 나타내는 클래스
    def __init__(self, src, dest, weight):
        self.src = src  # 간선의 시작 정점
        self.dest = dest  # 간선의 끝 정점
        self.weight = weight  # 간선의 가중치

    # 간선의 가중치를 기준으로 비교 연산을 정의 (정렬 시 사용)
    def __lt__(self, other):
        return self.weight < other.weight

# 특정 정점의 루트를 찾는 함수 (경로 압축 기법 적용)
def find(parent, i):
    if parent[i] == i:  # 자신이 루트인 경우
        return i
    else:
        # 재귀적으로 루트를 찾아 경로를 압축
        parent[i] = find(parent, parent[i])
        return parent[i]

# 두 집합을 합치는 함수 (유니온 연산)
def union(parent, x, y):
    rootX = find(parent, x)  # x의 루트 찾기
    rootY = find(parent, y)  # y의 루트 찾기
    if rootX != rootY:  # 루트가 다르면 두 집합을 합침
        parent[rootY] = rootX

def main():
    import sys
    input = sys.stdin.read  # 표준 입력 읽기
    data = input().splitlines()  # 줄 단위로 입력 분리

    N = int(data[0])  # 정점의 개수
    M = int(data[1])  # 간선의 개수

    edges = []  # 그래프의 간선을 저장할 리스트

    # 간선 정보 입력 받기
    for i in range(2, 2 + M):
        A, B, C = map(int, data[i].split())  # 간선의 시작점, 끝점, 가중치
        edges.append(Edge(A - 1, B - 1, C))  # 0-based index로 변환하여 저장

    edges.sort()  # 간선을 가중치 기준으로 오름차순 정렬

    parent = [i for i in range(N)]  # 초기 부모 배열 (자기 자신이 부모)

    mst_weight = 0  # 최소 스패닝 트리의 가중치 합
    for edge in edges:
        x = find(parent, edge.src)  # 간선의 시작 정점의 루트 찾기
        y = find(parent, edge.dest)  # 간선의 끝 정점의 루트 찾기

        if x != y:  # 루트가 다르면 사이클이 생성되지 않음
            union(parent, x, y)  # 두 집합을 합침
            mst_weight += edge.weight  # 간선의 가중치를 추가

    print(mst_weight)  # 최소 스패닝 트리의 가중치 출력

if __name__ == "__main__":
    main()
