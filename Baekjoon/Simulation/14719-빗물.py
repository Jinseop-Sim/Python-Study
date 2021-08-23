import sys

h, w = map(int, sys.stdin.readline().split())
space = list(map(int, sys.stdin.readline().split()))

maxH = 1

for i in range(len(space)): # 얘는 max index 기준으로 왼쪽에 있는 애들의 값 계산
    if maxH < space[i]:
        maxH = space[i]
        maxI = i

total = 0
temp = 0

for i in range(maxI + 1): # 얘는 max index 기준으로 오른쪽에 있는 애들의 값 계산
    if space[i] > temp:
        temp = space[i]
    total += temp

temp = 0

for i in range(w-1, maxI, -1):
    if space[i] > temp:
        temp = space[i]
    total += temp

print(total - sum(space))

"""
처음 풀어보는 시뮬레이션 문제이다.
근데 생각보다 그냥 수학적인 문제였던 것 같다.

가장 높은 기둥을 기준으로 그 다음으로 높은 기둥으로 싹 다 더한다.
예를 들어서 기둥의 높이가 3 0 1 4 라면, 3 + 3 + 3 + 4 를 해주는 것이다.
그 후에, 모든 기둥의 높이의 합을 빼주면, 빗물이 찰 수 있는 공간의 높이만 딱 나온다.

따라서 total엔 빗물이 찰 수 있는 공간을 채운 기둥의 높이의 합을 저장한다. (temp를 이용해서)
total에서 전체 기둥의 합 sum(space)를 빼주면, 신기하게도 딱 빗물이 찰 수 있는 공간만 나온다.
"""
