import java.util.*;
public class Main {
    static int countPartitions(int n) {
        int[] dp = new int[n + 1]; dp[0] = 1;
        for (int i = 1; i <= n; i++)
            for (int j = i; j <= n; j++)
                dp[j] += dp[j - i];
        return dp[n];
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) System.out.println(countPartitions(sc.nextInt()));
    }
}