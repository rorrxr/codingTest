import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int[][] arr = new int[n][2];
            for (int i = 0; i < n; i++) {
                arr[i][0] = sc.nextInt();
                arr[i][1] = sc.nextInt();
            }

            Arrays.sort(arr, Comparator.comparingInt(a -> a[0]));

            int count = 1;
            int best = arr[0][1];
            for (int i = 1; i < n; i++) {
                if (arr[i][1] < best) {
                    count++;
                    best = arr[i][1];
                }
            }
            System.out.println(count);
        }
    }
}