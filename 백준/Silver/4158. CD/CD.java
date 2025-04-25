import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            // 한 줄에서 N, M 값을 읽어옴
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()); // 상근이의 CD 개수
            int m = Integer.parseInt(st.nextToken()); // 선영이의 CD 개수

            // 종료 조건
            if (n == 0 && m == 0) break;

            int[] a = new int[n]; // 상근이의 CD 목록
            int[] b = new int[m]; // 선영이의 CD 목록

            // 상근이의 CD 번호 입력 받기
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(br.readLine());
            }

            // 선영이의 CD 번호 입력 받기
            for (int i = 0; i < m; i++) {
                b[i] = Integer.parseInt(br.readLine());
            }

            // 투 포인터 알고리즘을 이용하여 공통 CD 개수 계산
            int i = 0, j = 0, cnt = 0;

            while (i < n && j < m) {
                if (a[i] == b[j]) {
                    // 두 CD가 같으면 공통 CD이기 때문에 카운트 증가
                    cnt++;
                    i++;
                    j++;
                } else if (a[i] < b[j]) {
                    // a[i]가 작으면 a의 포인터 이동
                    i++;
                } else {
                    // b[j]가 작으면 b의 포인터 이동
                    j++;
                }
            }

            // 결과 출력
            System.out.println(cnt);
        }
    }
}
