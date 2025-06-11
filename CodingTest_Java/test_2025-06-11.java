import java.util.*;
import java.util.regex.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();  // n 무시
        String s = sc.nextLine();
        Matcher m = Pattern.compile("\\d+").matcher(s);
        long sum = 0;
        while (m.find()) sum += Long.parseLong(m.group());
        System.out.println(sum);
    }
}