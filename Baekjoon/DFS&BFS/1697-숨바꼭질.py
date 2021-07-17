from collections import deque

subin, bro = map(int, input().split())
MAX = 100000
queue = deque()
cnt = [0]*(MAX+1)

def bfs():
    queue.append(subin)

    while queue:
        x = queue.popleft()
        if x == bro:
            print(cnt[x])
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not cnt[nx]: # cnt[nx]가 0이면, 방문을 안했다는 것! 그러므로 1초 추가한다.
                cnt[nx] = cnt[x] + 1
                queue.append(nx) # BFS의 진행을 위한 다음 Queue 삽입.

bfs()

"""
연산자 끼워넣기 처럼 DFS로 풀어보려고 했으나
연산 시간이 너무 오래걸려 BFS가 훨씬 빠르고 적합하다고 판단.
즉 최단 경로 문제와 동일한 방식으로 풀이.
"""
