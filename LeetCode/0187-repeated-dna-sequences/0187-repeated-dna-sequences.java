import java.util.*;

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        // 이미 나온 10글자 부분 문자열 저장
        Set<String> set = new HashSet<>();
        // 중복으로 두 번 이상 나온 10글자 문자열 저장
        Set<String> result = new HashSet<>();
        
        // 전체 문자열을 순회하면서 길이를 10짜리 부분 문자열 추출
        for (int i = 0; i <= s.length() - 10; i++) {
            // 길이 10의 부분 문자열 추출
            String substring = s.substring(i, i + 10);
            
            // set에 추가 실패했다는 것은 이미 한 번 등장함
            // 따라서 result에 추가
            if (!set.add(substring)) {
                result.add(substring);
            }
        }

        // Set을 List로 변환하여 결과 반환
        return new ArrayList<>(result);
    }
}