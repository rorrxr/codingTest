class Solution {
    public int solution(int price) {
        int answer = 0;
        double discnt = 0.0; // 할인율
        if(price >= 500000){
            discnt = 0.2;
        }else if(price >= 300000){
            discnt = 0.1;
        }else if(price >= 100000){
            discnt = 0.05;
        }else{
            discnt = 0.0;
        }
        
        answer = (int)(price - (discnt * price));
        
        return answer;
    }
}