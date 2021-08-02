import sys

def backtrack(depth):
    if len(visit) == m:
        print(*visit)
    else:
        for i in range(depth, n+1):
            visit.append(i)
            backtrack(i)
            visit.pop()

n, m = map(int, sys.stdin.readline().split())
visit = []

backtrack(1)

"""
앞서 푼 N과 M에서 중복되는 수를 뽑아낼 수 있도록만 하면 되는 문제이므로, 조건문만 빼준다.
반복문을 이용해서 dfs를 진행하는 이유는?
조합이 아닌, 순열 문제이므로 순서가 다른 경우엔 다른 종류의 배열로 보기 때문이다.
"""
