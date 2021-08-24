import sys

num = int(sys.stdin.readline())
oper = list(sys.stdin.readline().strip())
arr = [[0]*(num) for _ in range(num)]
res = []
iter = 0

def sign(idx):
    sum = 0
    for i in range(idx, -1, -1):
        sum += res[i]
        if arr[i][idx] == '+' and s <= 0:
            return 0
        if arr[i][idx] == '0' and s != 0:
            return 0
        if arr[i][idx] == '-' and s >= 0:
            return 0
    return 1

def backtrack(depth):
    if depth == num:
        print(' '.join(map(str, res)))
        exit(0)
    for i in range(-10, 11):
        res.append(i)
        if sign(depth):
            backtrack(depth + 1)
        res.pop()

for i in range(num):
    for j in range(i, num):
        arr[i][j] = oper[iter]
        iter += 1

backtrack(0)

"""
조합으로도 풀어보고 여러모로 고민해봤지만, 백트래킹이 가장 적합한 문제였던 것 같다.
"""
