import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
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
}