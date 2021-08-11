import sys

n = int(sys.stdin.readline())
stack = []
oper = []
cnt = 1
trigger = True

for i in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num:
        stack.append(cnt)
        oper.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        oper.append('-')
    else:
        trigger = False
if trigger == False:
    print('NO')
else:
    for i in oper:
        print(i)

"""
stack은 수를 넣을 배열, oper은 연산자를 넣을 배열이다.

1. num을 입력받는다.
2. cnt가 들어온 num이 될 때 까지 while 문을 반복하는데, 이는 오름차순으로 push를 하는 동작과 같다.
3. 그럼 1부터 num까지의 수가 stack에 쌓여있을텐데, 이 때 stack의 제일 마지막(가장 먼저 pop() 되는 수)이 num과 같다면 pop 시킨다.

* 이 때 trigger가 False가 되어 NO가 출력될 조건은, 오름차순으로 push를 하면 수열을 만들 수가 없는 경우.
  즉, stack[-1] == num 인 경우가 없는 경우이다.
"""
