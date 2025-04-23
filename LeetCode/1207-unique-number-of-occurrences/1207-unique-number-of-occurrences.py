from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 각 숫자의 등장 횟수를 세기
        count_dict = Counter(arr)
        
        # 등장 횟수만 추출하여 리스트로 만들기
        frequency_list = list(count_dict.values())
        
        # 등장 횟수 리스트에서 중복을 제거하여 set과 비교
        # 길이가 같으면 모든 빈도가 유일함
        return len(frequency_list) == len(set(frequency_list))
