package Day3;

public class CalRemainder {

	// 정수 num1, num2가 매개변수로 주어질 때, 
	// num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
	
	static int solution(int num1, int num2) {
	    int answer = -1;
	    answer = num1 % num2;
	    return answer;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// 입출력 예 1
		int num1 = 3;
		int num2 = 2;
	    
	    System.out.println(solution(num1,num2));
	    
	    // 입출력 예 2
	    num1 = 10;
	    num2 = 5;
	    
	    System.out.println(solution(num1,num2));
	}

}
