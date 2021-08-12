import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if not len(queue):
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if not len(queue):
            print(1)
        if len(queue):
            print(0)
    elif com[0] == 'front':
        if not len(queue):
            print(-1)
        else:
            print(queue[0])
    elif com[0] == 'back':
        if not len(queue):
            print(-1)
        else:
            print(queue[-1])
 """
 큐의 동작원리를 표현한 간단한 코딩이다.
 """
