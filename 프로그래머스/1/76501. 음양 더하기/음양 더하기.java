class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int sum = 0;
        
        //배열 길이
        for(int i=0; i<absolutes.length; i++){
            
            if(signs[i] == true){
                sum += absolutes[i];
            }
            else if(signs[i] == false){
                sum -= absolutes[i];
            }
        }
        return sum;
    }
}