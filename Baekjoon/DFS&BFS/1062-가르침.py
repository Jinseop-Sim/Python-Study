import sys

def dfs(idx, depth):
    global result

    if depth == length-5: # 깊이가 최대가 되면 return을 해야하는 조건이다.
        cnt = 0
        for word in words: # 
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]: # 배운 알파벳으로 이루어져있지 않아서 알 수 없는 단어라면, check = False로 바꾸고 다음 단어로.
                    check = False
                    break
            if check: # Check가 False가 아니라는 것은, 배울 수 있는 단어라는 뜻! 따라서 cnt를 1 증가 시킨다.
                cnt += 1
        result = max(result, cnt)
        return

    for i in range(idx, 26):
        if not learn[i]: # a부터 z까지 아직 배우지 않은 알파벳을 하나씩 대입해본다.
            learn[i] = 1
            dfs(i, depth + 1)
            learn[i] = 0 # length - 5까지 문자열을 다 채우고, 하나 빼고 그 다음 문자열을 찾아보는 백트래킹.

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
    learn[ord(c) - ord('a')] = 1   # a, c, i, n, t는 무조건 배우는 알파벳이다.

dfs(0, 0)
print(result)

"""
백트래킹 문제였다... 어렵다.
"""
