class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'  # 모음 목록
        max_count = 0     # 최대 모음 수
        current_count = 0 # 현재 윈도우 내 모음 수
        left = 0          # 윈도우의 시작 인덱스

        for right in range(len(s)):
            # 오른쪽 문자 추가
            if s[right] in vowels:
                current_count += 1

            # 윈도우 크기가 k 초과일 경우, 왼쪽 문자 제거
            if right - left + 1 > k:
                if s[left] in vowels:
                    current_count -= 1
                left += 1  # 왼쪽 포인터 이동

            # 최대 모음 수 갱신
            max_count = max(max_count, current_count)

        return max_count
