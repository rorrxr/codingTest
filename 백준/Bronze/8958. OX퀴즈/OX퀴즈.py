N = int(input())

for i in range(N):
    ox = input()
    score = 0
    cnt = 0

    for char in ox:
        if char == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)