import sys
from itertools import combinations

num, length = map(int, sys.stdin.readline().split())
alphabet = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
word = []
alpha = ['a', 'c', 'i', 't', 'n']
maxcnt = 0

for _ in range(num):
    word.append(set(sys.stdin.readline().rstrip()[4:-4]).difference('a', 'c', 'i', 't', 'n'))

if length < 5:
    print(0)
    exit(0)

else:
    for x in list(combinations(alphabet, length-5)):
        cnt = 0
        for w in word:
            if not w.difference(x):
                cnt += 1
        maxcnt = max(maxcnt, cnt)

print(maxcnt)

"""
Set과 조합을 이용해서 풀었더니 시간초과가 났다.
"""
