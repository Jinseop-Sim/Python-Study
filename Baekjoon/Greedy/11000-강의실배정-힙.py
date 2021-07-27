import sys
from queue import PriorityQueue
import heapq

num = int(sys.stdin.readline())
time = []
clas = []

for _ in range(num):
    a, b = list(map(int, input().split()))
    time.append([a, b])

time.sort() # 강의를 시작 시간이 제일 빠른 순서부터 오름차순 정렬한다.

heapq.heappush(clas, time[0][1]) # 제일 빠른 강의가 끝나는 시간을 clas 배열에 집어 넣는다.

for i in range(1, num):
    if clas[0] <= time[i][0]: # 제일 빠른 강의가 끝나는 시간보다 시작시간이 느리다면, 강의실을 새로 만들 필요가 없다.
        heapq.heappop(clas) # 따라서 현재 시간을 pop시키고
        heapq.heappush(clas, time[i][1]) # 새로운 시간(강의실)을 clas 배열에 push한다.
    else:
        heapq.heappush(clas, time[i][1]) # 제일 빠른 강의가 끝나는 시간보다 시작시간이 빠르다면, 강의실을 새로 만들어야하므로, pop없이 push만 진행한다.

print(len(clas))

"""
필요한 '최소' 강의실 수를 구하는 문제, Greedy 알고리즘이다.
그러나 Heapq 모듈에 대한 개념을 알고 있으면 풀기가 수월하다.
"""
