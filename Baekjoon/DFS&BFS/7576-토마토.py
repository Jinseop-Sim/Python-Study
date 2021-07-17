from collections import deque

col, row = map(int, input().split())
box = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()

for _ in range(row):
    tomato = list(map(int, input().split()))
    box.append(tomato)

def bfs():
    num = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                num = max(num, box[nx][ny])
                queue.append([nx,ny])

    return num-1

for i in range(row):
    for j in range(col):
        if box[i][j] == 1:
            queue.append([i,j])

days = bfs()
cnt = 0

for i in range(row):
    for j in range(col):
        if box[i][j] == 0:
            cnt += 1

if cnt == 0 and days == -1:
    print(0)

elif cnt == 0:
    print(days)

elif cnt != 0:
    print(-1)

"""
간단한 BFS 응용 문제이다.
"""
