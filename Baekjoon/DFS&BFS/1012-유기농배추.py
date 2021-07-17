import sys
sys.setrecursionlimit(10000)

case = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global cnt
    graph[x][y] = '#'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 1:
            graph[nx][ny] = '#'
            dfs(nx, ny)
    return cnt

for _ in range(case):
    col, row, cab = map(int, input().split())

    graph = [[0] * col for _ in range(row)]
    cnt = 0
    count = []

    for _ in range(cab):
        y, x = map(int, input().split())
        graph[x][y] = 1

    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1:
                count.append(dfs(i, j))

    print(len(count))
    
  """
  DFS로 풀 수 있는 간단한 문제.
  """
