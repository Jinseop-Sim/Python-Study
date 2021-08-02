import sys

def backtrack(index, sum):
    global cnt
    if index >= num:
        return
    sum += part[index]
    print(sum)
    if sum == sol:
        cnt += 1
    backtrack(index+1, sum-part[index])
    backtrack(index+1, sum)

num, sol = map(int, sys.stdin.readline().split())
part = list(map(int, input().split()))
cnt = 0

backtrack(0, 0)
print(cnt)

"""
두 가지의 경우를 나눠서 dfs를 생각한다.

1. 수열을 진행할 때 자기 자신을 포함한다. ==> 이 경우는 -7 -3 / -7 -3 -2 / -7 -3 -2 5 / -7 -3 -2 5 8 이런 식으로 이어지는 부분합의 표현을 담당한다.
2. 수열을 진행할 때 자기 자신을 포함하지 않는다. ==> 이 경우는 -7 -3 / -7 -2 / -7 5 / -7 8 이런 식으로 띄엄띄엄의 부분합 표현이 가능하다.

상당히 흥미로운 백트래킹 문제였다.
"""
