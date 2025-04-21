import java.util.*;

public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        // Set을 사용하여 nums1의 중복을 제거하고 저장
        Set<Integer> set1 = new HashSet<>();
        for (int num : nums1) {
            set1.add(num);
        }

        // 결과를 저장할 Set
        Set<Integer> resultSet = new HashSet<>();
        for (int num : nums2) {
            // nums2의 요소가 nums1에도 있다면 결과 Set에 추가
            if (set1.contains(num)) {
                resultSet.add(num);
            }
        }

        // 결과 Set을 배열로 변환
        int[] result = new int[resultSet.size()];
        int i = 0;
        for (int num : resultSet) {
            result[i++] = num;
        }

        return result;
    }
}
