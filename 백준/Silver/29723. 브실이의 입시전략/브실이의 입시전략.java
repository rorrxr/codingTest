import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N: 수강한 과목 수, M: 요구 과목 수, K: 공개된 과목 수
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Map<String, Integer> subjectScores = new HashMap<>();
        Set<String> publicSubjects = new HashSet<>();

        // 과목과 점수 저장
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String subject = st.nextToken();
            int score = Integer.parseInt(st.nextToken());
            subjectScores.put(subject, score);
        }

        // 공개 과목 저장
        for (int i = 0; i < K; i++) {
            publicSubjects.add(br.readLine());
        }

        int minScore = 0;
        int maxScore = 0;

        List<Integer> privateScores = new ArrayList<>();

        for (Map.Entry<String, Integer> entry : subjectScores.entrySet()) {
            String subject = entry.getKey();
            int score = entry.getValue();

            if (publicSubjects.contains(subject)) {
                // 공개 과목은 무조건 포함
                minScore += score;
                maxScore += score;
            } else {
                // 비공개 과목 점수는 나중에 선택용으로 리스트에 저장
                privateScores.add(score);
            }
        }

        // 비공개 과목에서 (M - K)개 선택
        Collections.sort(privateScores); // 오름차순 정렬

        int selectCount = M - K;

        // 최소 점수: 낮은 점수부터 선택
        for (int i = 0; i < selectCount; i++) {
            minScore += privateScores.get(i);
        }

        // 최대 점수: 높은 점수부터 선택
        for (int i = 0; i < selectCount; i++) {
            maxScore += privateScores.get(privateScores.size() - 1 - i);
        }

        System.out.println(minScore + " " + maxScore);
    }
}