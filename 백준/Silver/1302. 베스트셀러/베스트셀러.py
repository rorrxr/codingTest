"""

문제
김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 
김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.

오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 
둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
"""

import sys

input = sys.stdin.readline

N = int(input())

book_dict = {}

for _ in range(N):
    book_name = input().strip()
    if book_name in book_dict:
        book_dict[book_name] += 1
    else:
        book_dict[book_name] = 1

# 가장 많이 팔린 횟수 찾기
max_count = max(book_dict.values())

# 가장 많이 팔린 책 중 사전순으로 가장 앞서는 제목 찾기
most_sold_books = [book for book, count in book_dict.items() if count == max_count]
most_sold_books.sort()

# 출력
print(most_sold_books[0])
