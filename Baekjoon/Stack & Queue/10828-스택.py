import sys

num = int(sys.stdin.readline().strip())
stack = []

for _ in range(num):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        stack.append(com[1])
    elif com[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
  """
  스택을 직접 구현해보는 문제였다.
  
  * 만약 시간초과가 뜬다면 입력에 sys.stdin.readline().strip()을 이용할 것!
  """
