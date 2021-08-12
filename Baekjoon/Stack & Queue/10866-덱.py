import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push_front':
        queue.appendleft(com[1])
    elif com[0] == 'push_back':
        queue.append(com[1])
    elif com[0] == 'pop_front':
        if not len(queue):
            print(-1)
        else:
            print(queue.popleft())
    elif com[0] == 'pop_back':
        if not len(queue):
            print(-1)
        else:
            print(queue.pop())
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
덱의 동작 구조를 구현했다.
"""
