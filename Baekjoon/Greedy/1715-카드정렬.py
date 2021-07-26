import sys
from queue import PriorityQueue

num = int(sys.stdin.readline())
queue = PriorityQueue()
for i in range(num):
    queue.put(int(sys.stdin.readline()))

val = 0

while True:
    if(queue.qsize() == 1):
        break
    a = queue.get()
    b = queue.get()
    val += (a+b)
    queue.put(a+b)

print(val)

"""
그리디 알고리즘과 유사한 Priority Queue를 이용한 알고리즘이다.
"""
