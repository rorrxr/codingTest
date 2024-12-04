"""
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 

0
주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다.

"""
import sys

input = sys.stdin.readline

# N: 단어의 개수

N = int(input())

# words: 단어를 저장할 list

words = []

# N개의 단어를 words list에 저장

for _ in range(N):
    # sys.stdin.readline()은 '\n\'을 포함하는 입력이기 때문에 연속으로 값을 입력받는 for문에서 에러가 발생했다.
    words.append(input().strip())

# words list에서 중복 단어 제거
words = list(set(words))

# 사전 순으로 정렬
words.sort() 
# 문자열 길이 순으로 정렬
words.sort(key=len)

# words list 출력

for word in words:
    print(word)