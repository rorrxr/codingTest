import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 파일 개수 입력
        int n = scanner.nextInt();
        scanner.nextLine();

        // 파일 이름들을 배열에 저장
        String[] files = new String[n];
        for (int i = 0; i < n; i++) {
            files[i] = scanner.nextLine();
        }
        scanner.close();

        // 파일 이름의 길이 
        int length = files[0].length();
        StringBuilder pattern = new StringBuilder();

        // 각 인덱스별로 문자 비교
        for (int i = 0; i < length; i++) {
            char currentChar = files[0].charAt(i); // 첫 번째 파일의 i번째 문자
            boolean isSame = true; // 모든 파일이 이 문자를 공유하는지 여부

            // 나머지 파일들과 비교
            for (int j = 1; j < n; j++) {
                if (files[j].charAt(i) != currentChar) {
                    isSame = false; // 하나라도 다르면
                    break;
                }
            }

            // 결과 패턴에 추가
            if (isSame) {
                pattern.append(currentChar); // 모두 같으면 해당 문자 추가
            } else {
                pattern.append('?'); // 다르면 ? 추가
            }
        }

        // 최종 패턴 출력
        System.out.println(pattern.toString());
    }
}
