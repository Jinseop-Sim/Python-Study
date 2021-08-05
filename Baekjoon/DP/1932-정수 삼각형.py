import sys

num = int(sys.stdin.readline())
tri = []
for _ in range(num):
    tri.append(list(map(int, input().split())))

for i in range(1, num):
    for j in range(len(tri[i])):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif i == j:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[num-1]))

"""
간단하게 메모장에 끄적여보 경우의 수 그대로 코딩을 하면 되는 DP문제 였다.
"""
