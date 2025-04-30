from typing import List

# 출근 희망 시각에 10분을 더하는 함수
def add_10_minutes(time: int) -> int:
    hour = time // 100       # 시 추출
    minute = time % 100      # 분 추출
    minute += 10             # 10분 추가
    if minute >= 60:         # 60분 이상이면 시간 올림
        hour += 1
        minute -= 60
    return hour * 100 + minute  # HHMM 형식으로 반환

# 메인 로직
def solution(schedules: List[int], timelogs: List[List[int]], startday: int) -> int:
    count = 0                # 상품 받을 직원 수
    n = len(schedules)       # 전체 직원 수

    for i in range(n):       # 직원별 반복
        allowed_time = add_10_minutes(schedules[i])  # 각 직원의 허용 출근 시간 계산
        success = True       # 상품 받을 자격 여부

        for j in range(7):   # 일주일 동안 반복
            weekday = (startday - 1 + j) % 7 + 1  # 현재 요일
            if weekday >= 6:  # 토, 일은 검사 대상 제외
                continue

            if timelogs[i][j] > allowed_time:  # 지각했다면
                success = False                # 상품 대상 제외
                break

        if success:         # 모든 평일에 정시에 출근했다면
            count += 1      # 상품 받을 수 있음

    return count
