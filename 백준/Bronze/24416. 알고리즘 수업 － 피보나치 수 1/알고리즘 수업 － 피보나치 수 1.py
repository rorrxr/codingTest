n = int(input())

def fibonacci(n):
    # f의 길이를 0 * n+1로 초기화
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    # for문의 범위를 n + 1까지
    for i in range (3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

def fibo(n):
  return n-2

print(fibonacci(n), fibo(n))