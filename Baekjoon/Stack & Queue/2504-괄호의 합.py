import sys

paren = list(sys.stdin.readline().strip())
stack = []
su = 0

for i in paren:
    if i == ')': # 문자열의 앞에서 부터 계속 stack에 저장을 해오다가 ']'을 만났다.
        temp = 0
        while len(stack) != 0: # Stack이 빌 때 까지 계속 반복한다.
            top = stack.pop() # Stack을 Pop 해주면서 자신의 짝인 '('를 찾는다.
            if top == '(':  # 제대로 된 짝을 만났다.
                if temp == 0:
                    stack.append(2) # 자기 이외의 괄호가 아무것도 없었다는 것. 그냥 2를 저장한다.
                else:
                    stack.append(2*temp) # 자신 이외의 괄호가 1개 이상 있었다는 것이다. ([]) 이런 형식인 것이다.
                break # 정상 작동했으므로, 다음 괄호로 넘어가야한다. break
            elif top == '[': # 갑자기 '['가 나왔다는 것은 잘못된 문자열이라는 것!
                print(0) # 0을 출력하고 그냥 끝낸다.
                exit(0)
            else:
                temp = temp + int(top) # '('도 아니고 ']'도 아닌 닫는 괄호(')', ']')일 경우 자신이 포함한 괄호가 또 있는 것.
    elif i == ']': # 문자열의 앞에서 부터 계속 stack에 저장을 해오다가 ']'을 만났다. 위와 같은 동작을 반복한다.
        temp = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3*temp)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                temp = temp + int(top)

    else:
        stack.append(i)

for i in stack:
    if i == '(' or i == '[': # 괄호가 남아있다는 것은 잘못된 문자열 이라는 것이다. 0을 출력 후 종료.
        print(0)
        exit(0)
    else:
        su += i # 숫자만 남아있다는 것은 제대로 된 문자열인 것. 위에서 나온 수들의 합을 구해주면 된다.

print(su)

"""
스택의 극한 응용 문제였다.
"""
