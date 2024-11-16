# 주의 개수 입력받기
n = int(input())

# 각 사람의 근무시간을 저장하는 딕셔너리
work_time = {}

# 근무 시간대에 따른 근무 시간 리스트
hours = [4, 6, 4, 10]


# 주의 개수만큼 반복
for _ in range(n):
    for shift in range(4): # 근무 시간대만큼
        # 이름 입력.
        shifts = input().split()

        for person in shifts:
            # 만약 근무자가 있다면
            if person != "-":
                # 딕셔너리에 근무자가 없다면
                if person not in work_time:
                    # 근무자를 추가하고 근무시간을 초기화
                    work_time[person] = 0

                # 근무 시간을 더함
                work_time[person] += hours[shift]

# work_time의 길이가 0이라면 "Yes"
if len(work_time) == 0:
    print("Yes")

else:
    # 가장 많이 근무한 사람의 근무시간
    max_time = max(work_time.values())

    # 가장 적게 근무한 사람의 근무시간 
    min_time = min(work_time.values())

    if max_time - min_time <= 12:
        # 기준이 12시간 이하라면 "Yes"
        print("Yes")
    else:
        # 기준이 12시간 이하가 아니라면 "No"
        print("No")