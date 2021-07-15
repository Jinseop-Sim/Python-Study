from collections import deque

row, col = map(int, input().split())
maps = []
dx = [-1, 1, 0, 0] # 좌 우 위 아래
dy = [0, 0, 1, -1] # 좌 우 위 아래
queue = deque() # Deque를 이용하면 시간복잡도를 매우 줄일 수 있다.

for _ in range(row):
    treasure = list(input())
    maps.append(treasure)

def bfs(x, y):
    queue.append([x, y]) # Queue에 좌표를 집어 넣어서 제일 앞 좌표부터 훑는다.
    visit = [[0]*col for _ in range(row)] # 방문한 지점을 표시하기 위해 동일한 크기의 Matrix를 만든다.
    visit[x][y] = 1
    num = 0 # 실시간으로 visit에서 받아온 Distance를 저장한다.

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상하좌우를 검색하는 반복문
            nx = x + dx[i] 
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if maps[nx][ny] == 'L' and visit[nx][ny] == 0: # 방문하지 않은 경우의 'L'만 검색
                    visit[nx][ny] = visit[x][y] + 1 # 이전 Node+1 의 값을 저장함으로써 거리 표시
                    num = max(num, visit[nx][ny]) # 가장 마지막에 저장되는 값이 최종거리이므로 max 함수 이용
                    queue.append([nx, ny]) # 이어서 이어서 탐색을 하기 위해 인접한 node들을 queue에 저장, 제일 뒤에 붙는다.
    return num-1 # 간선의 갯수와 같으므로 1을 빼주는 게 맞다.

path = 0
for i in range(row):
    for j in range(col):
        if maps[i][j] == 'L': # L로 표시되어있는 모든 육지를 시작점으로하는 최단거리를 모두 훑는 Brute Force이므로 이렇게 한다.
            path = max(path, bfs(i, j)) # 최단거리 중 가장 긴 값이므로 max 함수를 이용한다.

print(path)

"""
BFS를 응용해서 최단거리를 구하는 가장 간단한 문제이다.
"""
