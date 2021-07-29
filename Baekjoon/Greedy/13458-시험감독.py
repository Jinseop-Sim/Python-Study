import sys

num = int(sys.stdin.readline())
std = list(map(int, sys.stdin.readline().split()))
boss, vice = map(int, sys.stdin.readline().split())
res = 0

for i in std:
    i -= boss
    cnt = 1
    if i > 0:
        cnt += i // vice
        if i % vice != 0:
            cnt += 1
    res += cnt

print(res)

"""
간단하게 푼 풀이이다.
"""
