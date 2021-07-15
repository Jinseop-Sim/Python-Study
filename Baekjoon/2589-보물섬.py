from collections import deque

row, col = map(int, input().split())
maps = []
dx = [-1, 1, 0, 0] # 좌 우 위 아래
dy = [0, 0, 1, -1] # 좌 우 위 아래
queue = deque()

for _ in range(row):
    treasure = list(input())
    maps.append(treasure)

def bfs(x, y):
    queue.append([x, y])
    visit = [[0]*col for _ in range(row)]
    visit[x][y] = 1
    num = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if maps[nx][ny] == 'L' and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    num = max(num, visit[nx][ny])
                    queue.append([nx, ny])
    return num-1

path = 0
for i in range(row):
    for j in range(col):
        if maps[i][j] == 'L':
            path = max(path, bfs(i, j))

print(path)

"""
BFS를 응용해서 최단거리를 구하는 가장 간단한 문제이다.
"""
