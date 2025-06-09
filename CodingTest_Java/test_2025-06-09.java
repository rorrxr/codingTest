import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char[] arr = s.toCharArray();
        int sum = 0;
        boolean hasZero = false;
        for (char c : arr) {
            sum += c - '0';
            if (c == '0') hasZero = true;
        }
        if (!hasZero || sum % 3 != 0) System.out.println(-1);
        else {
            Arrays.sort(arr);
            for (int i = arr.length - 1; i >= 0; i--) System.out.print(arr[i]);
        }
    }
}