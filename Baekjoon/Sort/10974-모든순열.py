import math

n = int(input())
perm = []

for i in range(1, n+1):
    perm.append(i)

for iter in range(0, math.factorial(n)):

    print(perm)
    
    index = n-1
    while index > 0 and perm[index-1] >= perm[index]:
        index -= 1

    jndex = index-1
    while jndex < n-1 and perm[jndex+1] > perm[index-1]:
        jndex += 1

    perm[index-1], perm[jndex] = perm[jndex], perm[index-1]

    jndex = n-1
    while index < jndex:
        perm[index], perm[jndex] = perm[jndex], perm[index]
        index += 1
        jndex -= 1
        
 """
 모든 순열을 다 출력해주는 코드이다.
 다음 순열을 출력하는 코드를 조금만 응용하여 만들었다.
 """
