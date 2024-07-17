import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        String answer = "";
        
        for(int i = 0; i < a.length(); i++){
            char c = a.charAt(i);
            if(Character.isUpperCase(c)){ // 대문자라면
                answer += Character.toLowerCase(c); // 소문자로 변경
            }else{//소문자라면
                answer += Character.toUpperCase(c); //대문자로 변경
            }
        }
        System.out.println(answer);
        
    }
}