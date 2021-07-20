def dfs(depth):
    if depth == 6:
        print(*arr)
        return
    for i in range(n):
        print(arr)
        if check[i] != 0:
            continue
        arr.append(nums[i])
        check[i] = 1
        dfs(depth+1)
        arr.pop()
        for j in range(i+1, n):
            check[j] = 0
while True:
    lotto = list(map(int, input().split()))
    n, nums = lotto[0], lotto[1:]
    if n == 0:
        break
    arr = []
    check = [0]*n
    dfs(0)
    print()

"""
조합으로 풀었던 문제를 DFS(Backtracking)로 다시 풀어보았다.
"""
