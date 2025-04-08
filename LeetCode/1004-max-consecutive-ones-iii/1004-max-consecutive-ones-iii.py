from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # 윈도우의 왼쪽 포인터
        max_length = 0  # 최대 연속 1의 길이

        # 오른쪽 포인터를 이동하면서 윈도우 확장
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1  # 0을 만났을 때 flip 기회를 하나 사용

            # flip 기회를 초과한 경우 윈도우의 왼쪽을 이동시키며 0 제거
            while k < 0:
                if nums[left] == 0:
                    k += 1  # 왼쪽 포인터가 가리키는 값이 0이면 flip 기회 복구
                left += 1  # 왼쪽 포인터를 오른쪽으로 이동

            # 현재 윈도우의 길이를 계산하고 최대값 갱신
            max_length = max(max_length, right - left + 1)

        return max_length
