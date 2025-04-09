public class Solution {
    public boolean digitCount(String num) {
        // 0부터 9까지 각 숫자의 등장 횟수를 저장할 배열
        int[] count = new int[10];  

        // 각 숫자의 등장 횟수 세기
        for (int i = 0; i < num.length(); i++) {
            // 문자 '0'~'9'를 숫자로 변환해서 count 배열 증가
            count[num.charAt(i) - '0']++;  
        }

        // 각 인덱스에 해당하는 숫자의 등장 횟수와 값 비교
        for (int i = 0; i < num.length(); i++) {
            // 해당 인덱스에 요구되는 등장 횟수
            int expectedCount = num.charAt(i) - '0';  
            if (count[i] != expectedCount) {
                return false;  // 조건을 만족하지 않으면 false 반환
            }
        }

        return true;  // 모든 조건을 만족하면 true 반환
    }
}