import sys

num = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
money = 0
car = cost[0]

for i in range(num-1):
    if car > cost[i]:
        car = cost[i]
    money += car * dist[i]

print(money)

"""
왜 Greedy 문제인가?
그 때 그 때 비교를 하면서 뒤의 도시보다 작은 cost의 기름을 사용하므로, Greedy 문제이다.
"""
