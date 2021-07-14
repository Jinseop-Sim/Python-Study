com = int(input())
link = int(input())
graph = [[0]*(com+1) for _ in range (com+1)]
visit = [0]*(com+1)
start = 1

cnt = 0

for i in range(link):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(v):
    global cnt

    visit[v] = 1
    for i in range(1, com+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)
            cnt += 1

dfs(start)
print(cnt)

"""
간단한 DFS를 이용한 바이러스 감염 컴퓨터의 개수를 구하는 문제
"""
