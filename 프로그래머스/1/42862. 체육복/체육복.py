def solution(n, lost, reserve):
    # 중복 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
            lost_set.remove(student)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
            lost_set.remove(student)
    
    # 전체 학생 수 - 체육복 없는 학생 수
    return n - len(lost_set)