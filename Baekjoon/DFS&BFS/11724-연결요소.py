import sys
sys.setrecursionlimit(10000)

ver, link = map(int, input().split())

graph = [[0]*(ver+1) for _ in range(ver+1)]
visit = [0]*(ver+1)
cnt = 0

for _ in range(link):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

def dfs(i):
    visit[i] = 1
    for v in range(1, ver+1):
        if graph[i][v] == 1 and visit[v] == 0:
            dfs(v)

for i in range(1, ver+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)

"""
DFS를 이용해서 연결 요소의 수를 구하는 코드이다.
"""
