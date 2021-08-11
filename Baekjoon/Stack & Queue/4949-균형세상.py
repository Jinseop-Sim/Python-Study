import sys

while True:
    ps = input()
    if ps == '.':
        break
    temp = True
    stack = []
    for i in ps:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack:
        print('yes')
    else:
        print('no')
 
"""
스택의 응용문제이다. 난이도가 확실히 올라갔다.

1. 먼저 문자열을 받으며 (, [ 괄호들이 있으면 stack에 집어넣는다.
2. )와 ]는 반드시 (, [ 와 짝을 이뤄야 하므로
    2-1. i가 )일 경우, stack 안에 없거나 stack 안의 짝이 [ 일 경우, 제일 처음 설정해놓은 bool 값을 False로 바꾸고 for문을 탈출한다.
    2-2. i가 ]일 경우, 위와 같은 방식으로 진행한다.
    2-3. i가 짝이 맞는 경우, stack.pop()을 해서 짝이 맞는 괄호이므로 stack에서 비워준다.
3. 위의 경우에 탈출을 했을 때, temp가 True 이거나, stack이 비어있을 경우 'YES'를 출력한다.
4. Break로 탈출을 했을 경우, temp = False이고 Stack도 안비어있으므로, 'NO'를 출력한다.
"""
