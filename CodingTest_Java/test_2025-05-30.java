import java.util.*;
public class Main {
    static List<Integer>[] graph;
    static boolean[] visited;

    static void dfs(int v) {
        visited[v] = true;
        System.out.print(v + " ");
        for (int next : graph[v]) {
            if (!visited[next]) dfs(next);
        }
    }

    static void bfs(int v) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visitedBfs = new boolean[graph.length];
        q.add(v);
        visitedBfs[v] = true;
        while (!q.isEmpty()) {
            int cur = q.poll();
            System.out.print(cur + " ");
            for (int next : graph[cur]) {
                if (!visitedBfs[next]) {
                    visitedBfs[next] = true;
                    q.add(next);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), v = sc.nextInt();
        graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt(), w = sc.nextInt();
            graph[u].add(w);
            graph[w].add(u);
        }
        for (List<Integer> list : graph) if (list != null) Collections.sort(list);

        visited = new boolean[n + 1];
        dfs(v);
        System.out.println();
        bfs(v);
    }
}