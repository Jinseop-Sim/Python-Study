# Searching
---
## Binary Search(이진 탐색)
## Exhaustive Search(완전 탐색)
> 완전 탐색은 주어지는 데이터의 크기가 기본적으로 매우 작아야한다.  
> 그 이유는 시간 복잡도가 O(2^N)이나 O(N!)이므로 매우 시간이 오래걸리기 때문이다.  

### Brute Force
> Brute Force, 무차별 대입(공격)이라고 한다.  
> 가능한 경우의 수를 모두 대입해보는 공격이다.  
> 시간복잡도 O가 매우 커질 수 있으므로 굉장히 연산에 있어서 소모적인 공격이다.  
> 경우의 수를 대강 계산해 본 뒤 가능할 정도이면 사용을 하는 기법이다.  

### Permutation
> Permutation, 순열이다.  
> 확률과 통계에서 배웠던 그 순열이 맞다. 순서에 신경을 쓰며 자리를 옮기는 모든 경우를 말하는 것이다.  

![캡처](https://user-images.githubusercontent.com/71700079/124467025-42e35f00-ddd2-11eb-8135-31b55c4f827f.PNG)  

- 특이하게도 위의 순열을 관찰해보면, N개의 데이터가 있을 때, 1~i 번째 까지의 데이터를 설정을 했을 때  
  i 번째 데이터를 기준으로 최종 순열은 i+1부터 N까지가 모두 내림차순이라는 점이 특이하다.  
ex) 1 3 2 / 2 3 1 / 3 2 1
- 따라서 다음에 올 순열을 구하는 방법은 다음과 같다.

> 순열을 구성할 배열을 A라고 하고, index를 i와 j로 두자. 예로 A = [7,2,3,6,5,4,1]로 가정하겠다.  
> 1. A[i-1] <= A[i]를 만족하는 i중에 가장 큰 값을 찾는다. ==> 현재 i값을 기준으로 모두 내림차순으로 되는 경우를 찾는다는 것이다.  
>    A배열의 경우를 살펴보면 A[i-1] < A[i]가 되는 가장 큰 i는 6인 i = 3이 된다.  
>    
> 2. j >= i 중, A[j] > A[i-1]을 만족하는 가장 큰 j의 값을 찾는다.  
>    현재가 최종 순열 상태이므로, i-1 번째 숫자를 변경하여 최초 순열을 찾아야 한다.
>    A배열을 기준으로 i-1번째 숫자는 3으로 3보다 큰 경우는 6, 5, 4이고 그 중 j값이 가장 큰 경우는 4이다.  
>
> 3. A[i-1]과 A[j]를 Swap한다.  
>    i-1인 2번째 숫자 3과 j인 5번째 숫자 4를 변경한다.  
>    그럼 배열 A는 [7,2,4,6,5,3,1]이 된다.  
> 
> 4. A[i] 부터 순열을 모두 뒤집는다.  
>    최초 순열의 상태로 만드는 것이므로, i번째 부터는 오름차순으로 만든다.  
>    그럼 배열 A는 [7,2,4,1,3,5,6]이 된다.  
>    
> 위와 같은 순서로 반복 진행한다.

### Recursion
> 자기 자신을 호출하는 방식인 재귀의 이용.  
> 예를 들어, 100개의 숫자 중 5개를 중복없이 선택하는 경우의 수를 모두 출력을 하라고 한다면, 그냥 반복문 만을 이용해서 하기에는 시간복잡도가 기하급수적으로 늘어난다.  
> 따라서 이럴 때 재귀를 이용하면 시간복잡도를 대폭 줄일 수가 있다!  
> 예시 문제로는 하노이의 탑이나 백준의 연산자 끼워넣기 문제로 공부를 할 수 있다.

### DFS(Depth-First Searching)
> 연결된 노드들을 깊이를 우선으로 탐색을 하는 탐색 기법이다.  
> 백준의 연산자 끼워넣기 문제를 재귀로 풀었을 때 탐색하는 기법이, 대표적인 DFS 방식이다.  
> 보통 Stack을 이용하게 되며, 노드가 매우 깊거나, 데이터의 크기가 매우 큰 경우에는 지양해야한다.  
> 하지만 아래로 depth가 깊은 상황에서는 BFS보다 매우 빠른 속도로 탐색이 가능하다.  

![캡처](https://user-images.githubusercontent.com/71700079/124910125-322b2700-e026-11eb-9055-874cf5ef4d51.PNG)

- 대표 예시 문제 : 2667 - 단지번호 붙이기
```python
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
````

### BFS(Breadth-First Searching)
> 계층, 깊이 별로 순환탐색을 진행하는 넓이 우선 탐색 기법이다.  
> 깊이마다 노드들을 Queue에 차례대로 집어넣고 꺼내어 순환하는 형태이다. 즉 Queue를 이용한다.  
> 자식 노드의 자식 노드를 탐색하려 할 때 메모리의 낭비가 발생한다. Why? 아래로 내려가려면 옆으로 쭉 갔다가 와야하기 때문이다.  

![캡처](https://user-images.githubusercontent.com/71700079/124910382-7e766700-e026-11eb-9717-77396aa5a974.PNG)

- 대표 예시 문제 : 2667 - 단지번호 붙이기 BFS로 풀기.
```python
from collections import deque

def bfs(x, y):
    global cnt
    queue.append([x,y])
    home[x][y] = '#'
    cnt += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and home[nx][ny] == 1:
                queue.append([nx, ny])
                cnt += 1
                home[nx][ny] = '#'
    return cnt

n = int(input())
queue = deque()
home = []
danzi = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

for _ in range(n):
    apt = list(map(int, input()))
    home.append(apt)

for i in range(n):
    for j in range(n):
        if home[i][j] == 1:
            cnt = 0
            danzi.append(bfs(i,j))

print(*danzi)
````

### Backtracking
> 해를 찾아가는 도중에 이 노드가 해와 상관이 없겠다 싶으면 바로 가지치기를 하도록 하는 알고리즘  
> 더 이상 앞으로 나가지 않아도 되므로 반복문의 반복 횟수를 줄일 수 있다.  
> 주로 DFS 문제에서 전혀 답이 될 수 없는 경우는 반복하지 않도록 조건문을 걸어줌으로써 Bactracking을 구현한다.  
> 대표적 예시 : N-Queens Problem

- Promising : 해가 될 가능성이 있다. 유망하다.
- Pruning : 해가 될 가능성이 없다. 가지치기한다. (이 개념이 매우 중요하다!)

- 대표 예시 문제 : 9663 - N-Queens Problem
