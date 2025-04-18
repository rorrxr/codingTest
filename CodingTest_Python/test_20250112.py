# 문제 링크: https://www.acmicpc.net/problem/1074
def z(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n-1)
    if r < half and c < half:
        return z(n-1, r, c)
    elif r < half and c >= half:
        return half * half + z(n-1, r, c-half)
    elif r >= half and c < half:
        return 2 * half * half + z(n-1, r-half, c)
    else:
        return 3 * half * half + z(n-1, r-half, c-half)

N, r, c = map(int, input().split())
print(z(N, r, c))
