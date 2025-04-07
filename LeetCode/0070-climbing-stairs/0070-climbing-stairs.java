class Solution {
    public int climbStairs(int n) {
        // n이 1 또는 2일 경우는 직접 반환
        if (n <= 2) return n;

        // 피보나치 초기값 설정
        // f(1) = 1, f(2) = 2
        int first = 1;   // f(n-2)
        int second = 2;  // f(n-1)
        int third = 0;   // f(n)

        // 3부터 n까지 반복해서 f(n) 계산
        for (int i = 3; i <= n; i++) {
            third = first + second; // f(n) = f(n-1) + f(n-2)
            first = second;         // 다음 루프를 위해 업데이트
            second = third;
        }

        // 최종 결과 반환 (f(n))
        return third;
    }
}
