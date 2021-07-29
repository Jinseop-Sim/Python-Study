import sys

num = int(sys.stdin.readline())
std = list(map(int, sys.stdin.readline().split()))
boss, vice = map(int, sys.stdin.readline().split())
cnt = 0

for i in range(num):
    if std[i] > 0:
        std[i] -= boss
        cnt += 1

iter = 0
while True:
    minus = 0
    if std[iter] > 0:
        std[iter] -= vice
        cnt += 1
        iter += 1
        if iter == num:
            iter = 0
    else:
        iter += 1
        if iter == num:
            iter = 0
    for i in range(num):
        if std[i] <= 0:
            minus += 1
    if minus == num:
        break

print(cnt)

"""
연산시간이 굉장히 오래걸리는 풀이이다.
다른 방법을 연구해보자.
"""
