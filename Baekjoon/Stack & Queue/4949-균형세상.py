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
"""
