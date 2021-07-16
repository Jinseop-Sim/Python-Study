import itertools

n = int(input())
val = list(map(int, input().split()))
switch = []
oper = list(map(int, input().split()))
temp = oper[:]
usearr = oper[:]
max = -1000000000
min = 1000000000
cnt = 0

while temp[0] + temp[1] + temp[2] + temp[3] != 0:
    if temp[0] != 0:
        switch.append(1)
        temp[0] -= 1
    if temp[1] != 0:
        switch.append(2)
        temp[1] -= 1
    if temp[2] != 0:
        switch.append(3)
        temp[2] -= 1
    if temp[3] != 0:
        switch.append(4)
        temp[3] -= 1

perm = list(itertools.permutations(switch))

for sol in range(0, len(perm)):
    cons = val[0]
    for i in range(1, n):
        if perm[sol][i-1] == 1:
            if(usearr[0] != 0):
                cons += val[i]
                usearr[0] -= 1
                continue
        elif perm[sol][i-1] == 2:
            if(usearr[1] != 0):
                cons -= val[i]
                usearr[1] -= 1
                continue
        elif perm[sol][i-1] == 3:
            if(usearr[2] != 0):
                cons *= val[i]
                usearr[2] -= 1
                continue
        elif perm[sol][i-1] == 4:
            if(usearr[3] != 0):
                if cons < 0:
                    cons = abs(cons)
                    cnt = 1
                cons //= val[i]
                usearr[3] -= 1
                if cnt == 1:
                    cons = -cons
                    cnt += 1
                continue
    usearr = oper[:]
    if(max < cons):
        max = cons
    if(min > cons):
        min = cons

print(max)
print(min)

"""
1+2+3-4×5÷6 = 1
1÷2+3+4-5×6 = 12
1+2÷3×4-5+6 = 5
1÷2×3-4+5+6 = 7

위와 같이 N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.
"""

