import sys

def backtrack(depth):
    if len(visit) == m:
        print(*visit)
    else:
        for i in range(depth, n+1):
            if i in visit:
                continue
            visit.append(i)
            backtrack(i+1)
            visit.pop()

n, m = map(int, sys.stdin.readline().split())
visit = []

backtrack(1)

"""
나는 visit List를 일일히 다 검사해서 오름차순으로 정렬된 배열만 출력시켰는데
이 풀이는 아예 애초에 배열에 넣을 때 부터 오름차순으로 들어간다.
Argument로 depth를 추가해주어 visit[0]의 값이 1이면, 1 2 1 3 1 4 / 2이면, 2보다 큰 수인 3부터 2 3 2 4 / 3이면 3보다 큰 수인 3 4
이런 식으로 배열에 들어가게 된다. 4는 들어가봤자 뒤에 더 이상 수가 없으므로 돌지 않는다.
"""
