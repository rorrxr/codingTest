import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), x = sc.nextInt();
        boolean found = false;
        for (int i = 0; i < n; i++)
            if (sc.nextInt() == x) found = true;
        System.out.println(found ? 1 : 0);
    }
}