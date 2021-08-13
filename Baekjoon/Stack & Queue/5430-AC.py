import sys
from collections import deque

case = int(sys.stdin.readline())
for _ in range(case):
    func = list(sys.stdin.readline().strip())
    num = int(sys.stdin.readline())
    ser = eval(sys.stdin.readline())
    queue = deque(ser)

    temp = True
    cnt = 0

    for i in func:
        if i == 'R':
            cnt += 1
        else:
            if not queue:
                print('error')
                temp = False
                break
            if cnt%2 == 0:
                queue.popleft()
            else:
                queue.pop()
    if cnt%2 == 1:
        queue.reverse()

    if temp == True:
        print('[', end='')
        for i in range(len(queue)):
            print(queue[i], end='')
            if i != len(queue)-1:
                print(',', end = '')
        print(']')
"""
문자열을 입력받을 때, 문자가 포함되어 있어 숫자만 골라내야 할 경우, eval() 라이브러리 함수를 이용할 수 있다.
원래는 시간초과가 뜨는데 문자가 'RR' 연속 두 번 올 경우 굳이 뒤집을 필요가 없으므로 cnt 변수를 이용해 제어할 수 있다.
이를 통해 시간을 줄이는 것이 이 문제의 핵심!
"""
