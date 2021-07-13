def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while queue:
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n+1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
s = [[0]*(n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

print(s)

dfs(v)
print()
bfs(v)

"""
Depth-First Searching과 Breadth-First Searching의 가장 간단한 형태이다.
지점과 간선의 수를 받고 시작점을 입력으로 받아, 각 지점간의 이동 순서를 출력한다.
DFS와 BFS 둘 다.
"""
