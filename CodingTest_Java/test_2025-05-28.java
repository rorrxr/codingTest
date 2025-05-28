import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] meetings = new int[n][2];
        for (int i = 0; i < n; i++) {
            meetings[i][0] = sc.nextInt(); // 시작
            meetings[i][1] = sc.nextInt(); // 끝
        }

        Arrays.sort(meetings, (a, b) -> a[1] != b[1] ? a[1] - b[1] : a[0] - b[0]);

        int count = 0, end = 0;
        for (int[] m : meetings) {
            if (m[0] >= end) {
                count++;
                end = m[1];
            }
        }
        System.out.println(count);
    }
}