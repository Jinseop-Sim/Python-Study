import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
cnt = 0
queue = deque()
for i in range(n):
    queue.append(i+1)

print('<', end='')
while len(queue) > 0:
    cnt += 1
    if cnt%k == 0:
        print(queue.popleft(), end = '')
        if queue:
            print(', ', end='')
        continue
    queue.append(queue.popleft())
print('>')

"""
요세푸스 순열(n, k)의 문제이다.
사람이 n명이고 계속해서 k번째 사람을 죽여나가는 순열이다.
"""
