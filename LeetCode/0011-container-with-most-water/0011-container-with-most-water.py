class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 왼쪽과 오른쪽 포인터 초기화
        left, right = 0, len(height) - 1
        max_area = 0  # 최대 면적 초기화

        # 포인터가 겹치기 전까지 반복
        while left < right:
            # 현재 너비는 두 포인터 사이 거리
            width = right - left
            # 현재 높이는 두 수직선 중 더 낮은 값
            current_height = min(height[left], height[right])
            # 현재 면적 계산
            current_area = width * current_height
            # 최대 면적 갱신
            max_area = max(max_area, current_area)

            # 더 짧은 수직선을 안쪽으로 이동시킴
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area  # 최대 물의 양 반환