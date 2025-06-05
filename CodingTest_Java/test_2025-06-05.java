import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<String, Double> scores = Map.of(
            "A+", 4.5, "A0", 4.0, "B+", 3.5, "B0", 3.0,
            "C+", 2.5, "C0", 2.0, "D+", 1.5, "D0", 1.0, "F", 0.0
        );

        double total = 0, sum = 0;
        for (int i = 0; i < 20; i++) {
            String[] input = sc.nextLine().split(" ");
            double credit = Double.parseDouble(input[1]);
            if (input[2].equals("P")) continue;
            sum += credit * scores.get(input[2]);
            total += credit;
        }
        System.out.printf("%.6f", sum / total);
    }
}