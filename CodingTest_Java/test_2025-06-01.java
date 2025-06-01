import java.util.*;
public class Main {
    static List<Integer>[] graph;
    static boolean[] visited;

    static void dfs(int x) {
        visited[x] = true;
        for (int next : graph[x]) {
            if (!visited[next]) dfs(next);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        graph = new ArrayList[n + 1];
        visited = new boolean[n + 1];

        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            graph[u].add(v);
            graph[v].add(u);
        }

        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                dfs(i);
                count++;
            }
        }
        System.out.println(count);
    }
}