import sys
from queue import PriorityQueue

num = int(sys.stdin.readline())
time = []

for _ in range(num):
    a, b = list(map(int, input().split()))
    time.append([a, b])

time.sort()
queue = PriorityQueue()
queue.put((time[0][1], time[0][1])) # Queue에 제일 빠른 수업이 끝나는 시간을 집어넣는다.

for i in range(1, num):
    if queue.queue[0][1] <= time[i][0]: # Queue의 제일 빠른 수업이 끝나는 시간보다 시작시간이 빠른 수업이 없다면
        queue.get() # 강의실은 필요가 없으므로 get()으로 pop시킨다.
        queue.put((time[i][1], time[i][1])) # 그리고 새 시간(강의실)을 추가
    else:
        queue.put((time[i][1], time[i][1])) # 시작시간이 빠른 수업이 있다면, 강의실이 하나 더 필요하므로 get() 과정 없이 새 강의실 추가

print(queue.qsize())

"""
Heapq 모듈이 아닌 PriorityQueue 모듈을 이용한 풀이이다.
물론 PriorityQueue 모듈은 heapq 모듈을 기반으로 만들어졌다.
"""

