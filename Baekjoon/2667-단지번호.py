n = int(input())
home = []
danzi = []
dx = [-1, 1, 0, 0] # 좌 우 위 아래
dy = [0, 0, 1, -1] # 좌 우 위 아래
# 좌 우 위 아래를 확인해야하는 좌표문제는 dx, dy 리스트를 따로 만드는게 좋다!
cnt = 0

for _ in range(n):
    apt = list(map(int,input()))
    home.append(apt)
"""
방문한 곳은 # 으로 바꾸어 더 이상 1이 아닌 것으로 만든다.
1이 아니라면 방문했던 #은 dfs 함수가 작동하지 않는다. 
즉, 인접 단지만 계속 dfs가 작동하며 더 이상 인접 아파트가 없을 시, cnt가 초기화 되며
다음 1이 있는 좌표를 찾아서 다시 dfs 탐색을 시작한다.
"""
def dfs(x,y):
    global cnt
    home[x][y] = '#'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and home[nx][ny] == 1:
            home[nx][ny] = '#'
            dfs(nx, ny)
    return cnt

for a in range(n):
    for b in range(n):
        if home[a][b] == 1:
            cnt = 0
            danzi.append(dfs(a,b))

print(len(danzi))
danzi.sort()
for i in danzi:
    print(i)
