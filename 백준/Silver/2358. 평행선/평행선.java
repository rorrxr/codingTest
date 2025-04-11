/*
 * 문제
평면에 n개의 점이 있다. 그중 두 개 이상의 점을 지나면서 x축 또는 y축에 평행한 직선이 몇 개인지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 각 점의 좌표가 주어진다. 같은 좌표가 여러 번 주어질 수 있으며, 그런 경우 서로 다른 점으로 간주한다. 좌표는 절댓값이 231보다 작은 정수이다.

출력
첫째 줄에 답을 출력한다.
 */

 import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Map<Integer, Integer> xMap = new HashMap<>();
        Map<Integer, Integer> yMap = new HashMap<>();

        // 점의 좌표 입력
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            xMap.put(x, xMap.getOrDefault(x, 0) + 1);
            yMap.put(y, yMap.getOrDefault(y, 0) + 1);
        }

        int lineCount = 0;

        // x축에 평행한 직선 개수: y좌표가 같은 점이 2개 이상이면 +1
        for (int count : xMap.values()) {
            if (count >= 2) {
                lineCount++;
            }
        }

        // y축에 평행한 직선 개수: x좌표가 같은 점이 2개 이상이면 +1
        for (int count : yMap.values()) {
            if (count >= 2) {
                lineCount++;
            }
        }

        System.out.println(lineCount);
        sc.close();
    }
}
