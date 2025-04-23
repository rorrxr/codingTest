import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(); // 버스 개수
        int T = scanner.nextInt(); // 영식이 도착 시간

        int minWaitTime = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            int S = scanner.nextInt(); // 시작 시간
            int I = scanner.nextInt(); // 간격
            int C = scanner.nextInt(); // 대수

            // 각 버스의 출발 시각 계산
            for (int j = 0; j < C; j++) {
                int departureTime = S + I * j;
                if (departureTime >= T) {
                    minWaitTime = Math.min(minWaitTime, departureTime - T);
                    break; // 이 버스보다 늦은 건 더 기다림
                }
            }
        }

        if (minWaitTime == Integer.MAX_VALUE) {
            System.out.println(-1); // 탈 수 있는 버스 없음
        } else {
            System.out.println(minWaitTime);
        }
    }
}