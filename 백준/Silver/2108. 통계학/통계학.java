import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] numbers = new int[N];
        int sum = 0;

        // 빈도 계산용 배열 (문제 조건: -4000 이상 4000 이하)
        int[] freq = new int[8001];

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            numbers[i] = num;
            sum += num;
            freq[num + 4000]++;
        }

        Arrays.sort(numbers);

        // 1. 산술 평균
        System.out.println(Math.round((double) sum / N));

        // 2. 중앙값
        System.out.println(numbers[N / 2]);

        // 3. 최빈값
        int maxFreq = 0;
        for (int f : freq) {
            if (f > maxFreq) {
                maxFreq = f;
            }
        }

        List<Integer> modeList = new ArrayList<>();
        for (int i = 0; i < freq.length; i++) {
            if (freq[i] == maxFreq) {
                modeList.add(i - 4000);
            }
        }

        if (modeList.size() > 1) {
            Collections.sort(modeList);
            System.out.println(modeList.get(1)); // 두 번째로 작은 값
        } else {
            System.out.println(modeList.get(0));
        }

        // 4. 범위
        System.out.println(numbers[N - 1] - numbers[0]);
    }
}
