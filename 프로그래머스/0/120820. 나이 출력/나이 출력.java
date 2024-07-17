class Solution {
    public int solution(int age) {
        int answer = 0;
        if(age <= 23){
            answer = 2023 - age;
        }else if(age > 23){
            answer = (2023 - age);
        }
        return answer;
    }
}