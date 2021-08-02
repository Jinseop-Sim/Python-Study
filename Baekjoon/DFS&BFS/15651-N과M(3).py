import sys

def backtrack():
    if len(visit) == m:
        print(*visit)
    else:
        for i in range(1, n+1):
            visit.append(i)
            backtrack()
            visit.pop()

n, m = map(int, sys.stdin.readline().split())
visit = []

backtrack()

"""
백트래킹 문제였던 15649번 N과M(1) 문제에서, 조건문이 빠졌다.
그럼 중복된 수도 출력한다.
"""
