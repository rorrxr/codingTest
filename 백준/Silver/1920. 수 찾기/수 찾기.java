import java.util.*;
import java.io.*;

public class Main {
    // 이진 탐색 함수
    public static boolean binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] == target) {
                return true; // 값을 찾은 경우
            } else if (arr[mid] < target) {
                left = mid + 1; // 오른쪽 탐색
            } else {
                right = mid - 1; // 왼쪽 탐색
            }
        }
        return false; // 찾지 못한 경우
    }

    public static void main(String[] args) throws IOException {
        // 빠른 입력을 위한 BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 번째 줄: 정수 N
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];

        // 두 번째 줄: 배열 A
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // 배열 A를 정렬
        Arrays.sort(A);

        // 세 번째 줄: 정수 M
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        // 각 쿼리 값에 대해 이진 탐색 수행
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            int query = Integer.parseInt(st.nextToken());
            if (binarySearch(A, query)) {
                sb.append("1\n");
            } else {
                sb.append("0\n");
            }
        }

        // 결과 출력
        System.out.print(sb.toString());
    }
}
