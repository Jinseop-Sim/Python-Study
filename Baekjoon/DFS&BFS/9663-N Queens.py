import sys

def backtrack(depth):
    global cnt

    if depth == num:
        cnt += 1
        return

    for i in range(num):
        if not(col[i] or slash[depth+i]  or backslash[depth-i+num-1]):
            col[i] = slash[depth+i] = backslash[depth-i+num-1] = 1
            backtrack(depth + 1)
            col[i] = slash[depth+i] = backslash[depth-i+num-1] = 0


num = int(sys.stdin.readline())
col = [0]*num
slash = [0]*(2*num-1)
backslash = [0]*(2*num - 1)
cnt = 0

backtrack(0)

print(cnt)

"""
백트래킹 문제의 교과서 격인 N Queens 문제이다.
DP에 Knapsack 문제가 있다면, Backtracking에는 N Queens가 있다!

1. 좌우(행)은 확인을 할 필요가 없다. why? 퀸이 N개이므로 어차피 한 행에 최소 퀸 한 개씩 와야해서.
2. 상하(열)을 확인을 하기 위해 N칸의 col 배열을 만든다.
3. / 방향 대각선 요소들을 참조하기 위해서는 / 방향으로 쭉 동일한 값들을 가져야하므로, (x,y)가 좌표일 때 x+y가 모두 같음을 알 수 있다.
  why?) / 방향의 좌표들은 x+y 값이 모두 동일하다. e.g. (1,1) (0,2) (2,0)
  ==> 이를 위해서 2N-1 칸의 배열을 만든다. why?) 합의 값이 0 ~ 2N(N, N) 까지 나올 수 있기 때문
4. \ 방향 대각선 요소들을 참조하기 위해서는 \ 방향으로 쭉 동일한 값들을 가져야하므로, (x,y)가 좌표일 때 x-y+n-1이 모두 같음을 알 수 있다.
  why?) \ 방향의 좌표들은 x-y의 값이 모두 동일하다. e.g. (0,3) (1,4) (2,5)
  ==> 이를 위해서 2N-1 칸의 배열을 만든다. why?) 합의 값이 0 ~ 2N(N, 0) 까지 나올 수 있기 때문

depth == num이 되면 경우 하나가 끝난 것이므로 Count를 하나 올린다.

col[i]나 slash[depth+i]나 backslash[depth-i+num-1]이 0이면, 1로 바꿔 준다.
    why?) 좌표를 (depth, i)라고 생각을하면 된다!
          depth를 하나씩 늘려가며(열을 1씩 추가하며) 2, 3, 4번 경우에 해당하는 곳에 Queen이 없으면(0이면) 새 Queen을 놓는다(1로 바꾼다).
"""
