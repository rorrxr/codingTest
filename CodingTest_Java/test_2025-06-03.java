import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        int n = sc.nextInt();
        sc.nextLine();
        while (n-- > 0) {
            String cmd = sc.nextLine();
            if (cmd.startsWith("push")) stack.push(Integer.parseInt(cmd.split(" ")[1]));
            else if (cmd.equals("pop")) System.out.println(stack.isEmpty() ? -1 : stack.pop());
            else if (cmd.equals("size")) System.out.println(stack.size());
            else if (cmd.equals("empty")) System.out.println(stack.isEmpty() ? 1 : 0);
            else if (cmd.equals("top")) System.out.println(stack.isEmpty() ? -1 : stack.peek());
        }
    }
}