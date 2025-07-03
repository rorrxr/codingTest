import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력을 빠르게 받기 위한 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int K = Integer.parseInt(st.nextToken()); // 기존 랜선 수
        int N = Integer.parseInt(st.nextToken()); // 필요한 랜선 수

        int[] cables = new int[K];
        long maxLen = 0; // 랜선 중 최대 길이

        for (int i = 0; i < K; i++) {
            cables[i] = Integer.parseInt(br.readLine());
            if (cables[i] > maxLen) {
                maxLen = cables[i]; // 최대 길이 저장
            }
        }

        long start = 1;           // 최소 길이
        long end = maxLen;        // 최대 길이
        long result = 0;          // 가능한 최대 랜선 길이

        while (start <= end) {
            long mid = (start + end) / 2; // 자를 길이 기준
            long count = 0;

            // 모든 랜선에 대해 잘라낼 수 있는 개수 누적
            for (int cable : cables) {
                count += (cable / mid);
            }

            // N개 이상 만들 수 있다면 -> 더 긴 길이도 가능한지 확인
            if (count >= N) {
                result = mid;       // 가능한 길이 저장
                start = mid + 1;    // 더 긴 길이 탐색
            } else {
                end = mid - 1;      // 길이를 줄여서 탐색
            }
        }

        // 최종 결과 출력
        System.out.println(result);
    }
}
