from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 첫 번째로 작은 값과 두 번째로 작은 값을 무한대로 초기화
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                # num이 가장 작은 값이라면 first 갱신
                first = num
            elif num <= second:
                # num이 first보다는 크지만 second보다는 작으면 second 갱신
                second = num
            else:
                # num이 first와 second보다 모두 크면 조건 만족
                return True
        
        # 세 수를 만족하는 조합이 없으면 False 반환
        return False
