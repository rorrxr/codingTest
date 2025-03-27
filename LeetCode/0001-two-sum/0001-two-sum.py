from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 숫자의 보완값을 저장할 딕셔너리
        complements = {}
        
        # 배열의 모든 요소를 순회
        for i, num in enumerate(nums):
            # 현재 숫자와 합쳐서 target이 되는 보완값 계산
            complement = target - num
            
            # 보완값이 이미 딕셔너리에 있다면 정답을 반환
            if complement in complements:
                return [complements[complement], i]
            
            # 현재 숫자를 딕셔너리에 저장 
            complements[num] = i
        
        # 문제에서 항상 정답이 존재한다고 했으므로 이 리턴은 실행되지 않음
        return []