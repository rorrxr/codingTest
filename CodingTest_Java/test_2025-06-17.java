import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<Character> list = new LinkedList<>();
        for (char c : sc.nextLine().toCharArray()) list.add(c);
        ListIterator<Character> it = list.listIterator(list.size());
        int m = Integer.parseInt(sc.nextLine());
        while (m-- > 0) {
            String cmd = sc.nextLine();
            if (cmd.equals("L") && it.hasPrevious()) it.previous();
            else if (cmd.equals("D") && it.hasNext()) it.next();
            else if (cmd.equals("B") && it.hasPrevious()) { it.previous(); it.remove(); }
            else if (cmd.startsWith("P")) it.add(cmd.charAt(2));
        }
        StringBuilder sb = new StringBuilder();
        for (char c : list) sb.append(c);
        System.out.println(sb);
    }
}