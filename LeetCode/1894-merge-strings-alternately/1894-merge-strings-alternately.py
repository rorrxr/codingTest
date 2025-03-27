class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 두 문자열의 길이를 구합니다.
        len1, len2 = len(word1), len(word2)
        
        # 결과를 저장할 리스트를 초기화합니다.
        result = []
        
        # 두 문자열을 번갈아가며 추가합니다.
        for i in range(min(len1, len2)):
            result.append(word1[i])
            result.append(word2[i])
        
        # 남은 부분을 추가합니다.
        result.append(word1[i + 1:])
        result.append(word2[i + 1:])
        
        # 결과를 문자열로 변환합니다.
        return ''.join(result)