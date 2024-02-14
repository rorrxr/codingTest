package Day1;

public class CalSum {

	// 정수 num1과 num2가 주어질 때,
	// num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.

	static int solution(int num1, int num2) {
	    int answer = -1;
	    answer = num1 + num2;
	    return answer;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 입출력 예 1
		int num1 = 2;
		int num2 = 3;
	    
	    System.out.println(solution(num1,num2));
	    
	    // 입출력 예 2
	    num1 = 100;
	    num2 = 2;
	    
	    System.out.println(solution(num1,num2));
	}

}
