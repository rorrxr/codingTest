from collections import deque

class RecentCounter:
    def __init__(self):
        # 요청 시간을 저장할 deque 생성
        self.requests = deque()
        self.start_time = 0
        self.end_time = 0
        self.count = 0
        self.max_count = 0  # 최대 요청 수 저장

    def ping(self, t: int) -> int:
        # 새로운 요청 시간 t를 큐에 추가
        self.requests.append(t)

        # 유효한 시간 범위
        self.start_time = t - 3000
        self.end_time = t

        # 유효 범위 밖의 오래된 요청은 큐에서 제거
        while self.requests and self.requests[0] < self.start_time:
            self.requests.popleft()

        # 현재 유효한 요청 수 계산
        self.count = len(self.requests)

        # 지금까지의 최대 요청 수 갱신
        self.max_count = max(self.max_count, self.count)

        return self.count
    
    def getMaxCount(self) -> int:
        # 최대 요청 수 반환
        return self.max_count
