from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 투 포인터 초기화
        # slow는 0이 아닌 원소를 채울 위치
        # fast는 현재 탐색 중인 인덱스
        slow = 0
        fast = 0
        n = len(nums)
        
        # 0이 아닌 모든 원소를 앞쪽으로 이동
        while fast < n:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        # 남은 부분은 모두 0으로 채움
        for i in range(slow, n):
            nums[i] = 0