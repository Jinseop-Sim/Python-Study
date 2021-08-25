import sys

def dfs(idx, depth):
    global result

    if depth == length-5:
        cnt = 0
        for word in words:
            check = 1
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = 0
                    break
            if check:
                cnt += 1
        result = max(result, cnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i, depth + 1)
            learn[i] = 0

num, length = map(int, sys.stdin.readline().split())
if length<5:
    print(0)
    exit()
elif length == 26:
    print(num)
    exit()

result = 0
words = []
for _ in range(num):
    words.append(set(sys.stdin.readline().rstrip()))
learn = [0]*26

for c in ['a', 'c', 'i', 'n', 't']:
    learn[ord(c) - ord('a')] = 1

dfs(0, 0)
print(result)

"""
백트래킹 문제였다.
"""
