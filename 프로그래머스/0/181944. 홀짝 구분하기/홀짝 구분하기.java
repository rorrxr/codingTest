import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        if (n%2 == 0){ // 짝수라면
            System.out.println(n + " is even");
        }else if(n%2 == 1){ // 홀수라면
            System.out.println(n + " is odd");
        }else{
            System.out.println("NULL");
        }
        
    }
}