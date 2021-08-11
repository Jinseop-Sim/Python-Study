import sys

num = int(sys.stdin.readline())
stack = []

for _ in range(num):
    su = int(sys.stdin.readline())
    if su == 0:
        del stack[-1]
    else:
        stack.append(su)

print(sum(stack))

"""
스택을 이용하여 간단하게 풀 수 있었던 문제다.
"""
