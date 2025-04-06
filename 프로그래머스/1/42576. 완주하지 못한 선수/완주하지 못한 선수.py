def solution(participant, completion):
    # 다른 풀이 : 해시
    # counter = Counter(participant) - Counter(completion)
    # return list(counter.keys())[0]
    # Counter를 사용하면 간단하게 이름과 횟수를 세고, 차이 나는 이름을 추출할 수 있습니다.
    # 이 방법은 내부적으로 딕셔너리를 사용하므로 시간 복잡도는 **O(n)**로 더 빠를 수 있습니다.
    
    # 참가자와 완주자 리스트를 정렬합니다.
    participant.sort()
    completion.sort()

    # 정렬된 리스트에서 한 명씩 비교하면서 다른 사람을 찾습니다.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]  # 완주하지 못한 사람 발견

    # 모든 사람이 일치하면 마지막 참가자가 완주하지 못한 사람입니다.
    return participant[-1]