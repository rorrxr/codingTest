import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int y = 0, m = 0;
        for (int i = 0; i < n; i++) {
            int t = sc.nextInt();
            y += (t / 30 + 1) * 10;
            m += (t / 60 + 1) * 15;
        }

        if (y < m) System.out.println("Y " + y);
        else if (y > m) System.out.println("M " + m);
        else System.out.println("Y M " + y);
    }
}