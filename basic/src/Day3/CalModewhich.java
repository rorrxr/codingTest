package Day3;

public class CalModewhich {

	// 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
	// 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 
	// 최빈값이 여러 개면 -1을 return 합니다.
	static int solution(int[] array) {
        // https://iamdaeyun.tistory.com/entry/%EC%B5%9C%EB%B9%88%EA%B0%92-%EA%B5%AC%ED%95%98%EA%B8%B0-JAVA-%EC%9E%90%EB%B0%94-%EC%BD%94%ED%8C%85%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4
        int answer = 0; // 최빈값
        int max = 0;
        int[] count = new int[1000];
        
        for(int i=0; i<array.length; i++){
           count[array[i]]++;
        }
        
        for(int i = 0; i < count.length; i++){
            if(count[i] > max){
                max = count[i];
                answer = i;   
            }  
            // 최대값이 중복되면
            else if(count[i] == max){
                answer = -1;
            }
        }
           
        return answer;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int arr1[] = {1, 2, 3, 3, 3, 4};
		int arr2[] = {1, 1, 2, 2};
		int arr3[] = {1};

	    System.out.println(solution(arr1));
	    System.out.println(solution(arr2));
	    System.out.println(solution(arr3));

	}

}
