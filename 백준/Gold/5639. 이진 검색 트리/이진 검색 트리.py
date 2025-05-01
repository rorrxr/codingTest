
import sys
sys.setrecursionlimit(10**6)

# 전위 순회 결과를 저장할 리스트
preorder = []

# 빈 줄 제외하고 숫자만 추가
for line in sys.stdin:
    line = line.strip()
    if line:  # 빈 줄 무시
        preorder.append(int(line))

# 후위 순회 결과를 출력하는 함수
def dfs(start: int, end: int):
    if start > end:
        return

    root = preorder[start]

    # 루트보다 큰 값이 나오는 첫 지점
    split = end + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            split = i
            break

    dfs(start + 1, split - 1)  # 왼쪽 서브트리
    dfs(split, end)            # 오른쪽 서브트리
    print(root)                # 루트 출력

# 실행
dfs(0, len(preorder) - 1)
