class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 문자열이 서로를 나눌 수 없으면 공통된 패턴이 없음
        if str1 + str2 != str2 + str1:
            return ""

        # 유클리드 호제법으로 최대공약수 계산
        def compute_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        # 최대 공약수 길이 구하기
        gcd_length = compute_gcd(len(str1), len(str2))

        # 공통된 문자열 반환
        return str1[:gcd_length]