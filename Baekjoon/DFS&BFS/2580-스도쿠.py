import sys

sdoku = []
for _ in range(9):
    sdoku.append(list(map(int, sys.stdin.readline().strip().split())))
zero = [(i, j) for i in range(9) for j in range(9) if sdoku[i][j] == 0]

"""
zero = []
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            zero.append((i, j))  이 코드는 위의 zero = ... 코드와 동일하다.
"""

def checking(i, j):
    check = [1,2,3,4,5,6,7,8,9] # 빈 칸에 집어넣어 볼 9개의 숫자를 미리 list로 만들어 놓는다.

    for k in range(9):
        if sdoku[i][k] in check: # 가로를 검사해서 check에 이미 존재하는 숫자들을 모두 지운다.
            check.remove(sdoku[i][k])
        if sdoku[k][j] in check: # 세로를 검사해서 check에 이미 존재하는 숫자들을 모두 지운다.
            check.remove(sdoku[k][j])

    i //= 3  # 이 부분은 3*3 정사각형 내부를 검사하기 위한 파트이다.
    j //= 3  # 그냥 나누기가 아닌 몫으로 나누는 이유는, 정사각형이 유동적인 것이 아닌 고정이기 때문이다.

    for n in range(i*3, (i+1)*3):     # 3*3 정사각형은 3i 부터 3(i+1)까지. 즉 가로 3칸 세로 3칸을 검사.
        for m in range(j*3, (j+1)*3):
            if sdoku[n][m] in check:  # 검사를 해서 이미 존재하는 숫자라면 check에서 지운다.
                check.remove(sdoku[n][m])

    return check # check에 숫자가 남아있다면, 그 숫자는 가능한 숫자. 가능하지 않다면 check는 비어있을 것이다.

flag = False

def backT(index):
    global flag

    if flag:  # flag가 true이면 계산이 끝나고 답을 출력했다는 것. return시킨다.
        return

    if index == len(zero):  # index가 zero의 길이, 즉 0인칸을 다 채우면 답을 출력한다.
        for row in sdoku:
            print(*row)
        flag = True
        return
    else:  # 그게 아니라면 BackTracking을 적용한다.
        (i, j) = zero[index]  # (i, j)에 zero 배열에 있는 빈칸의 좌표를 받아온다.
        check = checking(i, j) #  checking 함수를 실행시킨 후 return된 숫자를 check 변수에 저장한다.

        for num in check: # return된 check 배열 내의 숫자를 sdoku 배열 내의 해당 좌표에 대입한다.
            sdoku[i][j] = num
            backT(index+1) # zero 배열 내의 좌표를 모두 완수할 때 까지 backtracking.
            sdoku[i][j] = 0  # 얘는 잘못된 경우로 갔을 때 이전단계로 돌아가도록 만든다.

backT(0)

"""
진짜 어려운 백트래킹(DFS) 문제였다.

먼저 백트래킹의 정의를 짚고 넘어가보자.
백트래킹이란 조건에 맞지 않는 경우를 살펴보지 않고 Proning(가지치기)를 하는 식의 알고리즘이다.
스도쿠를 예로 들면 검사한 라인에 같은 숫자가 하나라도 있으면, 더 이상 검사하지 않고 이전 단계로 돌아가는 것.

즉 스도쿠 문제를 풀기 위해서는, 검사를 위한 "Checking" 함수를 "BackT" 함수 내에서 작동시킨다.
"""
