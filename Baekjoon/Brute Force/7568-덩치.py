import sys

num = int(sys.stdin.readline())
inbody = []
a = []
rank = 1
for _ in range(num):
    inbody.append(list(map(int, sys.stdin.readline().split())))

for i in range(num):
    rank = 1
    for j in range(num):
        if i != j:
            if inbody[i][0] < inbody[j][0] and inbody[i][1] < inbody[j][1]:
                rank += 1
    a.append(rank)

print(*a)

"""
간단한 Brute Force 문제.
"""
