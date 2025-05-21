import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n], dp = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        dp[0] = arr[0];
        int max = dp[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(arr[i], dp[i - 1] + arr[i]);
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);
    }
}