# 문제 링크: https://www.acmicpc.net/problem/25206
import sys
input = sys.stdin.read
scores = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
lines = input().strip().split('\n')
total_score = 0
total_credits = 0
for line in lines:
    subject, credit, grade = line.split()
    if grade in scores:
        total_score += float(credit) * scores[grade]
        total_credits += float(credit)
print(round(total_score / total_credits, 6) if total_credits > 0 else 0.0)