package Day3;

import java.util.Arrays;

public class CalMiddleNum {
	// 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 
	// 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 
	// 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
    static int solution(int[] array) {
        int answer = 0;
        
        Arrays.sort(array);
        
        answer = array[array.length/2];
        
        return answer;
    }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int arr1[] = {1, 2, 7, 10, 11};
		int arr2[] = {9, -1, 0};
	    
	    System.out.println(solution(arr1));
	    System.out.println(solution(arr2));

	}

}
