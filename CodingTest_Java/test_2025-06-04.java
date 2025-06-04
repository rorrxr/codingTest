import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] minus = sc.nextLine().split("-");
        int result = Arrays.stream(minus[0].split("\\+")).mapToInt(Integer::parseInt).sum();
        for (int i = 1; i < minus.length; i++) {
            int temp = Arrays.stream(minus[i].split("\\+")).mapToInt(Integer::parseInt).sum();
            result -= temp;
        }
        System.out.println(result);
    }
}