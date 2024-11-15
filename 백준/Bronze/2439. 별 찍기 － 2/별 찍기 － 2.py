
N = int(input())

for i in range(N):
    # 공백
    print(" " * (N - i - 1), end = "")
    # 별
    print("*" * (i + 1))
