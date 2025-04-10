from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 숫자별 등장 횟수 세기
        count = Counter(nums)
        operations = 0

        for num in list(count.keys()):
            complement = k - num  # 짝이 되는 수

            # 만약 짝이 존재한다면
            if complement in count:
                if num == complement:
                    # 자기 자신과 짝이 되는 경우
                    operations += count[num] // 2
                else:
                    # 다른 수와 짝이 되는 경우
                    operations += min(count[num], count[complement])

                # 짝을 맞췄으므로 둘 다 0으로 처리
                count[num] = 0
                count[complement] = 0

        return operations
