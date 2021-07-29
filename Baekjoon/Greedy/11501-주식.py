import sys
case = int(sys.stdin.readline())
for _ in range(case):
    day = int(sys.stdin.readline())
    days = list(map(int, sys.stdin.readline().split()))
    sum = 0
    max = 0

    for i in range(len(days)-1, -1, -1):
        if days[i] > max:
            max = days[i]
        else:
            sum += max - days[i]

    print(sum)
    
"""
리스트를 역순회할 수 있다는 점을 생각해볼 수 있는 문제였다.
Greedy 알고리즘이다.
"""
