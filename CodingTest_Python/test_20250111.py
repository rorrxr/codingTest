# 문제 링크: https://www.acmicpc.net/problem/11478
s = input().strip()
substrings = {s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)}
print(len(substrings))