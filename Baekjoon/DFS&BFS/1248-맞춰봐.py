import sys

num = int(sys.stdin.readline())
oper = list(sys.stdin.readline().strip())
arr = [[0]*(num) for _ in range(num)] # 입력한 -와 + 부호를 2차원 배열에 저장하기 위해 만들어놓는 배열이다.
res = []
iter = 0

def sign(idx): # 현재 합의 부호가 arr 배열에 저장된 부호와 동일한지 확인하는 함수이다.
    sum = 0
    for i in range(idx, -1, -1): # 반복문 안에 집어 넣는 이유는, 뒤에서 부터 모든 상황에서의 합을 구해야 하기 때문에.
        sum += res[i]
        if arr[i][idx] == '+' and sum <= 0: # 합이 음수일 때는, arr이 '-' 여야하므로 양수나 0이면 False를 return한다.
            return 0
        if arr[i][idx] == '0' and sum != 0: # 합이 0일때는, arr이 '0' 이어야 하므로 False를 return한다.
            return 0
        if arr[i][idx] == '-' and sum >= 0: # 합이 양수일 때는 arr이 '+' 여야하므로 음수나 0이면 False를 return한다.
            return 0
    return 1 # 위의 조건을 다 피해가면, sum이 arr의 부호와 일치한다는 말이므로 True를 return한다.

def backtrack(depth):
    if depth == num: # Depth가 num과 같으면, 출력하고 함수에서 exit(0)로 탈출한다.
        print(' '.join(map(str, res)))
        exit(0)
    for i in range(-10, 11): # 규현이는 숫자 -10에서 10까지 21개의 숫자 밖에 모른다고 했다. 그 범위 내에서 Backtracking 하기 위해 반복문을 돌린다.
        res.append(i) 
        if sign(depth): # sign() 함수의 return 값이 1이면 depth+1을 해서 backtrack을 실행한다.
                        # depth에 1을 더하는 이유는? 뒤로 가면서 합을 구해야하기 때문이다.
            backtrack(depth + 1)
        res.pop() # 옳지 않은 수가 append 되었을 경우 위의 조건 검사 후 pop.

for i in range(num):
    for j in range(i, num):
        arr[i][j] = oper[iter] # Oper에 저장해놓은 값들을 arr 2차원 배열로 옮기는 과정이다.
        iter += 1

backtrack(0)

"""
조합으로도 풀어보고 여러모로 고민해봤지만, 백트래킹이 가장 적합한 문제였던 것 같다.
"""
