from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 0: # 빈 배열인 경우
            return 0

        write_index = 0  # 압축된 문자를 쓸 위치
        read_index = 0   # 현재 문자를 읽는 위치

        while read_index < n:
            char = chars[read_index]  # 현재 문자
            count = 0

            # 같은 문자가 반복되는 동안 count 증가
            while read_index < n and chars[read_index] == char:
                read_index += 1
                count += 1

            chars[write_index] = char
            write_index += 1

            # 반복 횟수가 2 이상인 경우
            if count > 1:
                for digit in str(count):  # 예: 12 -> '1', '2'
                    chars[write_index] = digit
                    write_index += 1

        return write_index
