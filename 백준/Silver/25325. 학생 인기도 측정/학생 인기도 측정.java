
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<String, List<String>> map = new HashMap<>();
        Map<String, Integer> popularity = new HashMap<>();
        String[] names = br.readLine().split(" ");
        for (String name : names) {
            map.put(name, new ArrayList<>());
            popularity.put(name, 0);
        }
        for (int i = 0; i < n; i++) {
            String[] likes = br.readLine().split(" ");
            for (String like : likes) {
                map.get(names[i]).add(like);
                popularity.put(like, popularity.get(like) + 1);
            }
        }
        List<Map.Entry<String, Integer>> list = new ArrayList<>(popularity.entrySet());
        Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                if (o2.getValue().equals(o1.getValue())) {
                    return o1.getKey().compareTo(o2.getKey());
                }
                return o2.getValue() - o1.getValue();
            }
        });
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Integer> entry : list) {
            sb.append(entry.getKey()).append(" ").append(entry.getValue()).append("\n");
        }
        System.out.print(sb.toString());
    }
}