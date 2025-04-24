/*
 * 문제
지훈이는 Sort 마스터다. 오랫동안 Sort 마스터 자리를 지켜온 지훈이는 이제 마스터 자리를 후계자에게 물려주려고 한다. 수많은 제자들 중에 후계자를 고르기 위해서 지훈이는 제자들에게 문제를 준비했다. 먼저 제자들에게 
$N$개의 원소를 가진 배열
$A$를 주고, 
$A$의 원소들이 오름차순으로 정렬된 배열
$B$를 만들게 한다. 그다음 
$M$개의 질문을 한다. 각 질문에는 정수 
$D$가 주어진다. 제자들은 주어진 정수
$D$가 
$B$에서 가장 먼저 등장한 위치를 출력하면 된다. 단, 
$D$가 
$B$에 존재하지 않는 경우에는 -1를 출력한다. Sort 마스터의 자리를 너무나도 물려받고 싶은 창국이를 위해 지훈이의 문제를 풀 수 있는 프로그램을 만들어 주자.

입력
첫째 줄에 배열
$A$의 원소의 개수 
$N$과 질문의 개수 
$M$이 공백으로 구분되어 주어진다.

다음 줄부터 
$N$줄에 걸쳐 정수 
$A_0, A_1, ... , A_{N-1}$이 주어진다.

다음 줄부터 
$M$줄에 걸쳐 정수 
$D$가 주어진다.

출력
 
$M$개의 질문에 대해서 주어진 
$D$가 
$B$에서 처음으로 등장한 위치를 출력한다. 단, 존재하지 않는다면 -1를 출력한다. (배열에서 가장 앞의 원소의 위치는 0이다.)
 */

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. N: 배열 A 크기, M: 질문 수
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        // 2. 배열 A 입력 받기
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }

        // 3. 배열 A를 정렬하여 B 생성
        int[] B = Arrays.copyOf(A, N);
        Arrays.sort(B);

        // 4. B에서 각 원소의 첫 등장 인덱스를 Map에 저장
        Map<Integer, Integer> valueToIndex = new HashMap<>();
        for (int i = 0; i < N; i++) {
            if (!valueToIndex.containsKey(B[i])) {
                valueToIndex.put(B[i], i);
            }
        }

        // 5. 질문 D에 대해 B에서의 첫 등장 인덱스를 출력
        for (int i = 0; i < M; i++) {
            int D = scanner.nextInt();
            System.out.println(valueToIndex.getOrDefault(D, -1));
        }

        scanner.close();
    }
}
