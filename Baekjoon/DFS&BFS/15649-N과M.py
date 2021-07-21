num, pick = map(int, input().split())
visit = []

def backtrack():
    if len(visit) == pick:
        print(*visit)
        return
    for i in range(1, num+1):
        if i in visit: # 이 조건은 visit에 같은 i가 2번 들어오는 경우, 즉 중복을 없애기 위한 조건.
            continue
        visit.append(i)
        backtrack() # visit의 길이가 pick과 같으면 바로 출력시켜 버리므로, 깊이는 2를 넘지 않는다.
        visit.pop() # 하나씩 제외시켜서 그 다음 i를 집어넣는 식.

backtrack()


"""
백트래킹을 연습하려고 푼 코드이다.
좀 더 연습이 필요할 것 같다.
"""
