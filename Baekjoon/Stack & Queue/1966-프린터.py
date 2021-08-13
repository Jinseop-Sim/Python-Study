import sys
from collections import deque

case = int(sys.stdin.readline())

for _ in range(case):
    n, m = map(int, sys.stdin.readline().split())
    impor = list(map(int, sys.stdin.readline().split()))
    queue = deque()
    for i in impor:
        queue.append(i)
    paper = [0]*n
    paper[m] = 1
    cnt = 0

    while True:
        if queue[0] == max(queue):
            cnt += 1 # 제일 중요한 문서이므로 출력, 카운트 올린다.
            if paper[0] == 1: # 얘가 우리가 찾는 문서가 맞나요?
                print(cnt) # 맞으면 출력 후 정지
                break
            else: # 아니면 출력을 했으므로 하나씩 지워준다.
                queue.popleft()
                del paper[0]
        else:
            queue.append(queue.popleft()) # 제일 앞에 있는게 중요한 문서가 아니면 큐의 제일 뒤로 보낸다.
            paper.append(paper[0])
            del paper[0]
