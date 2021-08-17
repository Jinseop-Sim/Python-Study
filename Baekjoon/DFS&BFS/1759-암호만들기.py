import sys

def backtrack(idx):
    if len(visit) == num:
        vow = 0
        con = 0
        for i in range(num):
            if visit[i] in 'aeiou':
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(visit))
        return

    for i in range(idx, char):
        if check[i] == 0:
            visit.append(code[i])
            check[i] = 1
            backtrack(i+1)
            check[i] = 0
            visit.pop()

num, char = map(int, sys.stdin.readline().split())
code = list(sys.stdin.readline().strip().split())
visit = []
check = [0]*char
code.sort()

backtrack(0)

"""
Backtracking 문제이다.

1. 문제의 조건에는 모음이 1개 이상 무조건 들어가야한다고 했다. ==> vow로 조정
2. 자음 또한 2개 이상 무조건 들어가야 한다 ==> con으로 조정
3. 알파벳의 순서에 맞춰서 출력이 되어야한다. ==> sort() 메서드로 정렬 후 idx를 늘려가며 출력한다.
  3-1. a가 들어오고 c가 들어오고 i가 들어오고 s가 붙고 출력.
  3-2. Bactrack 한 후 a c i t 출력, w 까지 출력 후 a c까지 Bactrack
  3-3. a c에 t를 붙여서 출력 후 s 출력. 계속 같은 식으로 반복된다.
 
==> 결국 순서를 신경쓰고 순열을 뽑아내는 백트래킹인데, 모음과 자음에 대한 조건이 들어간 문제였다.
// 참고 : 6603 - 로또
"""
