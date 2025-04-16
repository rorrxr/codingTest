import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<String> list = new ArrayList<>();
        Set<String> set = new HashSet<>(); // 중복 제거를 위한 HashSet
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            list.add(str);
            set.add(str);
        }
        list.clear(); // 중복 제거 후 리스트 초기화
        list.addAll(set); // 중복 제거된 단어들로 리스트 채우기
        Collections.sort(list, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() == o2.length()) {
                    return o1.compareTo(o2); // 길이가 같으면 사전 순으로 정렬
                }
                return Integer.compare(o1.length(), o2.length()); // 길이로 정렬
            }
        });
        StringBuilder sb = new StringBuilder();
        for (String str : list) {
            sb.append(str).append("\n");
        }
        System.out.print(sb.toString());
    }
}
