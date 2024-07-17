class Solution {
    public String solution(String s) {
        String answer = "";
        /*
        int max;
        int min;
        int num;
        
        String[] str = s.split("");
        for(int i = 0; i < str.length; i++){
            if(str[i].equals(" ")){
                num += i;
            }
            // 최대값
            if(str[i] > num){
                max += str[i];
            }
            
            // 최소값
            if(str[i] < num){
                min += str[i];
            }
        }
        */
        
        String[] numbers = s.split(" ");
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for(int i = 0; i < numbers.length; i++){
            int number = Integer.parseInt(numbers[i]);
            
            min = Math.min(min, number);
            max = Math.max(max, number);
        }

        answer = min+ " " +max;
        
        return answer;
    }
}