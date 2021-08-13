import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
where = deque(i for i in range(1, n+1))
cnt = 0

for sol in num:
    while True:
        if where[0] == sol:
            where.popleft()
            break
        else:
            if where.index(sol) <= len(where)//2:
                where.append(where.popleft())
                cnt += 1
            else:
                where.appendleft(where.pop())
                cnt += 1

print(cnt)

"""
deque의 기능을 최소한으로 이용한 풀이이다.
rotate() method도 있지만 사용하지 않았다.
index() method를 사용하지 않으면 코드가 매우 길어질 것 같아 사용했다.
"""
