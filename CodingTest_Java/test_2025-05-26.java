import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] coords = new int[n][2];
        for (int i = 0; i < n; i++) {
            coords[i][0] = sc.nextInt(); // x
            coords[i][1] = sc.nextInt(); // y
        }

        Arrays.sort(coords, (a, b) -> a[1] != b[1] ? a[1] - b[1] : a[0] - b[0]);

        for (int[] c : coords) {
            System.out.println(c[0] + " " + c[1]);
        }
    }
}