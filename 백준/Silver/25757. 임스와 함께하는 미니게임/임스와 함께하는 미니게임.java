/**
 * 문제
임스가 미니게임을 같이할 사람을 찾고 있습니다.

플레이할 미니게임으로는 윷놀이 
$Y$, 같은 그림 찾기 
$F$, 원카드 
$O$가 있습니다. 각각 2, 3, 4 명이서 플레이하는 게임이며 인원수가 부족하면 게임을 시작할 수 없습니다.

사람들이 임스와 같이 플레이하기를 신청한 횟수 
$N$과 임스가 플레이할 게임의 종류가 주어질 때, 최대 몇 번이나 임스와 함께 게임을 플레이할 수 있는지 구하시오.

임스와 여러 번 미니게임을 플레이하고자 하는 사람이 있으나, 임스는 한 번 같이 플레이한 사람과는 다시 플레이하지 않습니다.

임스와 함께 플레이하고자 하는 사람 중 동명이인은 존재하지 않습니다. 임스와 lms0806은 서로 다른 인물입니다.

입력
첫 번째 줄에는 사람들이 임스와 같이 플레이하기를 신청한 횟수 
$N$과 같이 플레이할 게임의 종류가 주어진다. 
$(1 \le N \le 100\,000)$ 

두 번째 줄부터 
$N$개의 줄에는 같이 플레이하고자 하는 사람들의 이름이 문자열로 주어진다. 
$(1 \le$ 문자열 길이 
$\le 20)$ 

사람들의 이름은 숫자 또는 영문 대소문자로 구성되어 있다.

출력
임스가 최대로 몇 번이나 게임을 플레이할 수 있는지 구하시오.
 */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력을 받기 위한 BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N: 신청한 횟수, gameType: 게임 종류
        int N = Integer.parseInt(st.nextToken());
        String gameType = st.nextToken();

        // HashSet을 사용하여 중복 제거된 플레이어 이름 저장
        Set<String> players = new HashSet<>();

        for (int i = 0; i < N; i++) {
            players.add(br.readLine().trim()); // 이름 저장
        }

        // 중복 제거된 유저 수
        int playerCount = players.size();
        int gameSize = 0;

        // 게임 종류에 따라 필요한 최소 인원 설정
        switch (gameType) {
            case "Y":
                gameSize = 2; // 윷놀이
                break;
            case "F":
                gameSize = 3; // 같은 그림 찾기
                break;
            case "O":
                gameSize = 4; // 원카드
                break;
        }

        // 임스 1명을 포함한 gameSize 명이 모이면 한 판 가능
        // 전체 인원 수를 gameSize로 나눈 몫이 최대 플레이 횟수
        System.out.println(playerCount / (gameSize - 1));
    }
}
