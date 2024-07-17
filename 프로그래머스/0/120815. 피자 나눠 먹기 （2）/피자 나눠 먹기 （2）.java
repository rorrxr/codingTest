class Solution {
    public int solution(int n) {
        int answer = 0;
        
        // 초기값 1
        for (int i = 1 ; i <= n ; i++){
            if((6 * i)% n == 0){
                answer = i;
                break; //만족할 경우 함수 자체를 탈출하도록함
            }
        }
        
//출처: https://dhdh-study.tistory.com/95 [dh.log:티스토리]
        /*
        //6의 배수(2로 나눠떨어지는 동시에 3으로 나눠떨어지는 수)
        if(n % 6 == 0 && n % 3 ==0){
            answer = n/2;
        }
        //3으로 나눠떨어지지만 2로 나눠떨어지지 않는 수
        else if(n % 3 == 0 && n % 2 != 0){
            answer = (n/6);
        }
        //2로 나눠 떨어지지만 3으로 나눠 떨어지지 않는 수
        else if(n % 2 == 0 && n % 3 != 0){
            answer = (n/6)+1;
        }
        //2로 나눠 떨어지지도 않고 3으로도 나눠 떨어지지 않는 수
        else if(n % 2 != 0 && n % 3 != 0){
            answer = (n/6) + 3;
        }else{
            System.out.println("다시 입력");
        }

        */
        return answer;
    }
}