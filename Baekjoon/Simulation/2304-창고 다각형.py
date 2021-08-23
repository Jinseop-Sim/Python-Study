import sys

num = int(sys.stdin.readline())
coord = []
max = 0
maxI = 0

for _ in range(num):
    x, y = map(int, sys.stdin.readline().split())
    coord.append([x,y])
    if max < y:
        max = y
        maxI = x

coord.sort()

pillar = [0]*(coord[-1][0] + 1)

for l, h in coord:
    pillar[l] = h

total = 0
temp = 0

for i in range(maxI+1):
    if pillar[i] > temp:
        temp = pillar[i]
    total += temp

temp = 0

for i in range(coord[-1][0], maxI, -1):
    if pillar[i] > temp:
        temp = pillar[i]
    total += temp

print(total)

"""
빗물과 똑같은 문제이다.

pillar = [0]*(coord[-1][0] + 1)

for l, h in coord:
    pillar[l] = h

이 부분이 핵심 포인트이다.
포문의 iterator은 두 개여도 된다는 것을 배웠다.
"""
