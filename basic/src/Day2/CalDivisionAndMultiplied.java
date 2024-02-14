package Day2;

public class CalDivisionAndMultiplied {
	// 정수 num1과 num2가 매개변수로 주어질 때, 
	// num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
	static int solution(int num1, int num2) {
	    int answer = 0;
	   
	    answer = (int) ((double)num1/(int)num2*1000);
	    return answer;
	}
	public static void main(String[] args) {
		// 입출력 예 1
		int num1 = 3;
		int num2 = 2;
	    
	    System.out.println(solution(num1,num2));
	    
	    // 입출력 예 2
	    num1 = 7;
	    num2 = 3;
	    
	    System.out.println(solution(num1,num2));
	    
	    // 입출력 예 3
	    num1 = 1;
	    num2 = 16;
	    
	    System.out.println(solution(num1,num2));
	}
}
