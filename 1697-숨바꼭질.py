from collections import deque

subin, bro = map(int, input().split())
MAX = 100000
queue = deque()
cnt = [0]*100

def bfs():
    queue.append(subin)

    while queue:
        x = queue.popleft()
        if x == bro:
            print(cnt[x])
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not cnt[nx]:
                cnt[nx] = cnt[x] + 1
                queue.append(nx)

bfs()

"""
DFS로 풀어보려 했으나, 너무 시간이 오래걸리는 관계로
최단 경로 문제와 동일하다고 생각하여 BFS로 풀었다.
"""
