import java.util.Arrays;

class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        Arrays.sort(arr2); // 이진 탐색을 위해 arr2 정렬
        int count = 0;

        for (int num : arr1) {
            if (isDistanceValue(num, arr2, d)) {
                count++; // 조건을 만족하면 count 증가
            }
        }

        return count;
    }

    // num과 arr2의 원소 사이에 거리가 d 이하인 값이 있으면 false
    private boolean isDistanceValue(int num, int[] arr, int d) {
        int left = 0, right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // 거리 조건에 맞지 않으면 false
            if (Math.abs(num - arr[mid]) <= d) {
                return false;
            }
            // arr[mid]가 num보다 너무 작으면 오른쪽 탐색
            else if (arr[mid] < num - d) {
                left = mid + 1;
            }
            // arr[mid]가 num보다 너무 크면 왼쪽 탐색
            else {
                right = mid - 1;
            }
        }

        return true; // 모든 값과의 거리가 d보다 큼
    }
}
