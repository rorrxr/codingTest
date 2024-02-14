package Day2;

public class ArrayMultiplied2 {

	// 정수 배열 numbers가 매개변수로 주어집니다. 
	// numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
	
	static int[] solution(int[] numbers) {
		int[] answer = new int[numbers.length];
		
        for(int i = 0; i < numbers.length; i++){
            answer[i] = numbers[i]*2;
        }
        return answer;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr1[] = {1, 2, 3, 4, 5};
		int arr2[] = {1, 2, 100, -99, 1, 2, 3};
	    
	    System.out.println(solution(arr1));
	    System.out.println(solution(arr2));
	}

}
