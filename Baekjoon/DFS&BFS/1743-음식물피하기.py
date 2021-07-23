from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue.append([x, y])
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and visit[nx][ny] == 0 and hall[nx][ny] == 1:
                queue.append([nx, ny])
                cnt += 1
                visit[nx][ny] = 1
    return cnt

row, col, num = map(int, input().split())
hall = [[0]*(col) for _ in range(row)]
visit = [[0]*(col) for _ in range(row)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sol = 0
queue = deque()

for i in range(num):
    x, y = map(int, input().split())
    hall[x-1][y-1] = 1

for i in range(row):
    for j in range(col):
        if hall[i][j] == 1:
            visit[i][j] += 1
            sol = max(sol, bfs(i, j))

print(sol)

"""
간단한 BFS를 이용한 문제이다.
"""
