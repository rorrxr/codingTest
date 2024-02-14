package Day1;

public class CalMultiplied {

	// 정수 num1, num2가 매개변수 주어집니다. 
	// num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.
	static int solution(int num1, int num2) {
	    int answer = 0;
	    
	    answer = num1 * num2;
	    return answer;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num1 = 3;
		int num2 = 4;
	    
	    System.out.println(solution(num1,num2));
	    
	    // 입출력 예 2
	    num1 = 27;
	    num2 = 19;
	    
	    System.out.println(solution(num1,num2));
	}

}
