import sys

case = int(sys.stdin.readline())

for _ in range(case):
    cnt = 0
    ps = list(sys.stdin.readline().strip())
    for i in ps:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt>0:
        print('NO')
    elif cnt == 0:
        print('YES')

"""
스택의 응용 문제이다. 
열린 괄호를 1, 닫힌 괄호를 -1로 놓고 그 합으로 판단한다.
"""
