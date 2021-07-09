n = int(input())
disas = 666
cnt = 0

while True:
    if '666' in str(disas):
        cnt += 1
    if cnt == n:
        print(disas)
        break
    disas += 1
 
"""
Brute Force 방식으로 문제를 해결한다.
disas를 666부터 1씩 올리는데, str(disas) Type Casting을 이용해 문자열 내에 666이 있으면 카운트롤 올린다.

if '666' in str(disas):

카운트가 n이 되면 탈출.
"""
