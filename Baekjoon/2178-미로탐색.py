from collections import deque

row, col = map(int, input().split())
maze = []
visit = [[0]*col for _ in range(row)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
visit[0][0] = 1

for i in range(row):
    a = list(map(int, input()))
    maze.append(a)

def bfs(x, y):
    queue.append([x,y])
    while queue:
        x, y = queue.popleft()

        if x == row-1 and y == col-1:
            print(visit[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if visit[nx][ny] == 0 and maze[nx][ny] == 1:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append([nx,ny])

bfs(0, 0)

"""
간단한 BFS 최단 경로 탐색 문제이다.
visit을 따로 만들지 않고 그냥 maze에서 BFS 탐색을 할 경우 첫 1이 3으로 바껴버린다.
따라서 visit matrix를 따로 만들어서 진행할 것!
"""
