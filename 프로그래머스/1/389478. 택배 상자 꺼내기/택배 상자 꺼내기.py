def solution(n, w, num):
    # 몇 층 필요한지
    h = (n + w - 1) // w

    # 박스 배열 만들기
    boxes = [[0]*h for _ in range(w)]

    cnt = 1
    for floor in range(h):
        if floor % 2 == 0:  # 왼쪽에서 오른쪽
            for col in range(w):
                if cnt <= n:
                    boxes[col][floor] = cnt
                    cnt += 1
        else:  # 오른쪽에서 왼쪽
            for col in range(w-1, -1, -1):
                if cnt <= n:
                    boxes[col][floor] = cnt
                    cnt += 1

    # num의 위치 찾기
    for col in range(w):
        for floor in range(h):
            if boxes[col][floor] == num:
                # 해당 열에서 위층부터 현재 층까지 상자 수 세기
                count = 0
                for f in range(floor, h):
                    if boxes[col][f] != 0:
                        count += 1
                return count
