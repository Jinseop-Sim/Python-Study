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
풀이 등록 예정
"""
