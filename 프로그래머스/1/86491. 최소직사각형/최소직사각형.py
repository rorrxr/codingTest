def solution(sizes):
    max_width = 0
    max_height = 0

    for size in sizes:
        width, height = size
        if width < height:
            width, height = height, width  # 가로가 더 크도록 설정
        max_width = max(max_width, width)
        max_height = max(max_height, height)

    return max_width * max_height