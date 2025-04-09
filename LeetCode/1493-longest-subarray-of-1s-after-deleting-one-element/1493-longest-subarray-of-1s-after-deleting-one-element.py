class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0  # 왼쪽 포인터
        max_length = 0  # 결과값
        zero_count = 0  # 현재 윈도우 내 0의 개수
        
        for right in range(len(nums)):
            # 오른쪽 포인터를 이동하면서 0의 개수 세기
            if nums[right] == 0:
                zero_count += 1
            
            # 윈도우 내 0이 2개 이상일 경우 왼쪽 포인터 이동
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # 최대 길이 갱신
            max_length = max(max_length, right - left)
        
        return max_length
