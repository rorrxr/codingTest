package Day2;

public class CalCompare {

	// 정수 num1과 num2가 매개변수로 주어집니다. 
	// 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
	static int solution(int num1, int num2) {
	    int answer = 0;
	    if(num1 == num2){
	        answer = 1;
	    }else{
	        answer = -1;
	    }
	    return answer;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 입출력 예 1
		int num1 = 2;
		int num2 = 3;
	    
	    System.out.println(solution(num1,num2));
	    
	    // 입출력 예 2
	    num1 = 11;
	    num2 = 11;
	    
	    System.out.println(solution(num1,num2));
	    
	    // 입출력 예 3
	    num1 = 7;
	    num2 = 99;
	    
	    System.out.println(solution(num1,num2));
	}

}
