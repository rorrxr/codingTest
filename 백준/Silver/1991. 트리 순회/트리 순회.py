class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, value):
        self.value = value  # 노드의 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

# 전위 순회 함수 (루트 -> 왼쪽 -> 오른쪽)
def pre_order_traversal(node):
    if node is None:
        return
    print(node.value, end='')  # 현재 노드 출력
    pre_order_traversal(node.left)  # 왼쪽 서브트리 순회
    pre_order_traversal(node.right)  # 오른쪽 서브트리 순회

# 중위 순회 함수 (왼쪽 -> 루트 -> 오른쪽)
def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)  # 왼쪽 서브트리 순회
    print(node.value, end='')  # 현재 노드 출력
    in_order_traversal(node.right)  # 오른쪽 서브트리 순회

# 후위 순회 함수 (왼쪽 -> 오른쪽 -> 루트)
def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.left)  # 왼쪽 서브트리 순회
    post_order_traversal(node.right)  # 오른쪽 서브트리 순회
    print(node.value, end='')  # 현재 노드 출력

def main():
    import sys
    input = sys.stdin.read  # 표준 입력 읽기
    data = input().splitlines()  # 줄 단위로 입력 받기

    N = int(data[0])  # 노드의 개수
    nodes = {}  # 노드 정보를 저장할 딕셔너리

    # 입력 데이터를 바탕으로 트리 구성
    for i in range(1, N + 1):
        node_info = data[i].split()  # 각 줄의 데이터 분리
        root = node_info[0]  # 루트 노드 값
        left = node_info[1]  # 왼쪽 자식 노드 값
        right = node_info[2]  # 오른쪽 자식 노드 값

        # 루트 노드 생성 (없으면 새로 생성)
        if root not in nodes:
            nodes[root] = TreeNode(root)
        rootNode = nodes[root]

        # 왼쪽 자식 노드 연결
        if left != '.':  # '.'은 자식 노드가 없음을 의미
            if left not in nodes:
                nodes[left] = TreeNode(left)
            rootNode.left = nodes[left]

        # 오른쪽 자식 노드 연결
        if right != '.':
            if right not in nodes:
                nodes[right] = TreeNode(right)
            rootNode.right = nodes[right]

    root = nodes['A']  # 트리의 루트는 항상 'A'
    
    # 전위 순회 출력
    pre_order_traversal(root)
    print()
    
    # 중위 순회 출력
    in_order_traversal(root)
    print()
    
    # 후위 순회 출력
    post_order_traversal(root)
    print()

if __name__ == "__main__":
    main()
