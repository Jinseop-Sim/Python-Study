import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())

"""
간단한 큐(덱) 문제이다.

queue.append(queue.popleft()) 라는 표현이 참 참신했던 문제이다.
queue.pop()이라는 메서드는 단순히 덱에서 빼는 것이 아니라 그 자체로 값을 갖는 다는 사실을 알아야만 풀 수 있다.
"""
