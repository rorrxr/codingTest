import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), t = sc.nextInt();
        boolean pass = true;
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            if (x > t) pass = false;
        }
        System.out.println(pass ? "Yes" : "No");
    }
}