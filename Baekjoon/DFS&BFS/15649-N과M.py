num, pick = map(int, input().split())
visit = []

def backtrack():
    if len(visit) == pick:
        print(*visit)
        return
    for i in range(1, num+1):
        if i in visit:
            continue
        visit.append(i)
        backtrack()
        visit.pop()

backtrack()


"""
백트래킹을 연습하려고 푼 코드이다.
좀 더 연습이 필요할 것 같다.
"""
