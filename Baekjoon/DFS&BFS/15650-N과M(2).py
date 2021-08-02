import sys

def backtrack():
    if len(visit) == m:
        cnt = 0
        for i in range(1, len(visit)):
            if visit[i] > visit[i-1]:
                cnt = 0
            else:
                cnt = 1
                break
        if cnt == 0:
            print(*visit)
    else:
        for i in range(1, n+1):
            if i in visit:
                continue
            visit.append(i)
            backtrack()
            visit.pop()

n, m = map(int, sys.stdin.readline().split())
visit = []

backtrack()

"""
기존의 백트래킹 N과 M에다가
이제는 오름차순으로 정리된 친구들만 출력하는 문제였다.
"""
