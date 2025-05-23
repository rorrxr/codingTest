import java.util.*;
public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int[] dp = new int[Math.max(3, n + 1)];
        dp[1] = 1;
        dp[2] = 3;

        for (int i = 3; i <= n; i++)
            dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007;

        System.out.println(dp[n]);
    }
}