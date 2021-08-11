n = int(input())
candy = [list(input()) for i in range(n)]
max = 0

def width():
    global max

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if candy[i][j] == candy[i][j-1]:
                cnt += 1
            else:
                if max<cnt:
                    max=cnt
                cnt = 1
        if max<cnt:
            max = cnt

def height():
    global max

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if candy[j][i] == candy[j-1][i]:
                cnt += 1
            else:
                if max<cnt:
                    max = cnt
                cnt = 1
        if max < cnt:
            max = cnt

for i in range(n):
    for j in range(1, n):
        candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]
        width()
        height()
        candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]

for i in range(n):
    for j in range(1, n):
        candy[j][i], candy[j-1][i] = candy[j-1][i], candy[j][i]
        width()
        height()
        candy[j][i], candy[j - 1][i] = candy[j - 1][i], candy[j][i]

print(max)

"""
가장 처음에 N×N크기에 사탕을 채워 놓는다. 
사탕의 색은 모두 같지 않을 수도 있다. 
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

간단한 Brute Force 문제이다.
"""
