import java.util.*;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        // Map을 사용하여 숫자별 등장 횟수를 세기
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : arr) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // 등장 횟수만 Set에 넣어서 중복 확인
        Set<Integer> occurrences = new HashSet<>();
        for (int freq : countMap.values()) {
            // 이미 존재하는 경우라면 중복된 횟수 존재하기 때문에 false 반환
            if (!occurrences.add(freq)) {
                return false;
            }
        }

        // 3. 모든 등장 횟수가 유일함
        return true;
    }
}
