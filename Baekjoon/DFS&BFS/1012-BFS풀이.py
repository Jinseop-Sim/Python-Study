from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue.append([x,y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx,ny])

col, row, cab = map(int, input().split())

graph = [[0] * col for _ in range(row)]
cnt = 0
count = []
queue = deque()

for _ in range(cab):
    y, x = map(int, input().split())
    graph[x][y] = 1

for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:
            graph[i][j] = 0
            bfs(i, j)
            cnt += 1

print(cnt)

"""
DFS로는 단지번호 붙이기처럼 반복문이 한번 끝날 때 마다 cnt를 올려주었는데,
BFS로는 그냥 graph를 순회하는 동안 0으로 바꾸면서 1을 몇번 만나는지만 세어주면 된다.
"""
