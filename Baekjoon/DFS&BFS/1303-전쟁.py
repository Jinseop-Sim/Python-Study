from collections import deque

def bfs(x, y, color): # 한칸 씩 BFS를 진행하는 전형적인 함수.
    cnt = 0
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if field[nx][ny] != 0 and field[nx][ny] == color:
                    queue.append([nx, ny])
                    field[nx][ny] = 0 # 0으로 바꾸어 B도 W도 아닌 칸으로 만들어서, for문에서 들어오지 못하게 한다.
                    cnt += 1
    return 1 if cnt == 0 else cnt

col, row = map(int, input().split())
field = []
cntw = 0
cntb = 0
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(row):
    a = list(input())
    field.append(a)

for i in range(row):
    for j in range(col):
        if field[i][j] != 0:
            if field[i][j] == 'W': # 필드의 병사가 W이면 W만 수집한다.
                cntw += bfs(i, j, field[i][j])**2 # Color의 칸에 W아니면 B를 집어넣은 다음 반환된 카운트를 제곱.
            else:
                cntb += bfs(i, j, field[i][j])**2

print(cntw, cntb)

"""
BFS를 이용하여 좌표를 읽는 문제였다.
"""
