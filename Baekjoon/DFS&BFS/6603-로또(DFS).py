def backtrack(depth):
    if depth == 6:
        return
    for i in range(n):
        if check[i] != 0: # 중복된 수를 넣지 않기 위한 체크 배열.
            continue
        visit.append(num[i])
        check[i] = 1
        print(visit)
        backtrack(depth+1) # 각 자리는 depth를 나타낸다.
        visit.pop()
        for k in range(i+1, n): # 끝날 때 마다 check를 비워주어야 중복이 안됐는데 출력을 못하는 경우가 없다.
            check[k] = 0

while True:
    lotto = list(map(int, input().split()))
    n, num = lotto[0], lotto[1:]
    if n == 0:
        break
    visit = []
    check = [0] * n
    backtrack(0)
    print()

"""
조합으로 풀었던 문제를 DFS(Backtracking)로 다시 풀어보았다.
"""
