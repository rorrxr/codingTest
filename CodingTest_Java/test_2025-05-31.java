import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        boolean[] visited = new boolean[n + 1];
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        visited[1] = true;

        int count = 0, depth = 0;
        while (!q.isEmpty() && depth < 2) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int cur = q.poll();
                for (int next : graph[cur]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        q.add(next);
                        count++;
                    }
                }
            }
            depth++;
        }

        System.out.println(count);
    }
}