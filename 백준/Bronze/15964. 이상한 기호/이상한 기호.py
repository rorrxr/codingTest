# A@B = (A+B)×(A-B)

def cal(a, b):
    if(a >= 1000 or b >= 1000):
      return
    else:
      return (a+b)*(a-b)

a, b = map(int, input().split())
print(cal(a, b))