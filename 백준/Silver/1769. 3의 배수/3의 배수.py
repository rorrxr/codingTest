# 문제분석
# 다른 문제로 바꾸어 풀기

# 문제 1. "양의 정수 X는 3의 배수인가?"

#  X의 각 자리의 수를 단순히 더한 수 Y를 만든다. 
# 예를 들어 X가 1107이었다면, Y는 1+1+0+7=9가 된다. 그리고 Y에 대해서, 아래와 같은 문제를 생각한다.

# 문제 2. "Y는 3의 배수인가?"

# 위의 문제 1의 답은 아래의 문제 2의 대답과 일치한다. 
# 위의 예의 경우, Y=9는 3의 배수이므로 X=1107 역시 3의 배수가 되는 것이다. 
# 214는 각 자리수의 합 2+1+4=7이 3의 배수가 아니므로 3의 배수가 아니다.

# 문제 변환의 과정을 몇 번 반복할지에 대한 조건
# 2단계에서 각자리의 합이 한자리수가 될 때까지 반복

# 입력 
# 첫 줄 : 자연수 X가 들어온다. 

# 출력
# 문제 변환 과정을 몇 번 거쳤는지를 출력한다. 이 수는 음이 아닌 정수가 되어야 한다. 
# 둘 째 줄에는 주어진 수가 3의 배수이면 YES , 아니면 NO를 출력한다.  

#################################

# 3의 배수인지 아닌지를 구한다
# 나눴을 때 3의 배수가 아니라
# 각 자리의 수를 더하고
# 그 더한 수를 나눴을 때 3의 배수인가

# 각 자리의 수를 더했을 때 각 자리의 수가 두자리 수가 아니어야 함
# 또 다시 반복하여 한자리수가 나올 때까지

# 입력
N = int(input()) # N = 1234 #문제의 핵심은 형변환 이라고 생각해요. int/str을 번갈아 

cnt = 0

while N >= 10 :
    # 각 자리수의 합을 더하는

    # 1. 숫자로 값을 입력받았죠
    # 2. 이걸 각 자릿수마다 접근하려면 string으로 한번 변환하는 과정이 필요하다고 생각했어요
    # 3. 그 분리한 각 자릿수 애들을 다시 integer로 형변환을 시켜줘서 더할 수 있게 만들어준거죠

    # N = 1234567
    # N = 1+2+3+4+5+6+7 =28
    # [1,2,3,4,5,6,7]

    N = sum(map(int, str(N)))
    cnt += 1
    
# 3의 배수인지
if N % 3 == 0:
    print(cnt)
    print("YES")
else:
    print(cnt)
    print("NO")