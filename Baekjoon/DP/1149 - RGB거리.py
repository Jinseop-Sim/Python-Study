import sys

num = int(sys.stdin.readline())
home = []

for _ in range(num):
    home.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(home)):
    home[i][0] = min(home[i-1][1], home[i-1][2]) + home[i][0] #빨간집
    home[i][1] = min(home[i-1][0], home[i-1][2]) + home[i][1] #초록집
    home[i][2] = min(home[i-1][0], home[i-1][1]) + home[i][2] #파란집
    print(home)

print(min(home[num-1][0], home[num-1][1], home[num-1][2]))


"""
DP 문제 였습니다.

집이 3채라고 가정할 때

1. home[2][0]에 저장되는 것은, 마지막 빨강 + 그 이전 파랑(그 이전 빨강 or 초록과 합) or 초록(그 이전 빨강 or 파랑과 합)
2. home[2][1]에 저장되는 것은, 마지막 초록 + 그 이전 빨강(그 이전 파랑 or 초록과 합) or 그 이전 파랑(그 이전 초록 or 빨강과 합)
3. home[2][2]에 저장되는 것은, 마지막 파랑 + 그 이전 빨강(그 이전 파랑 or 초록과 합) or 그 이전 초록(그 이전 빨강 or 파랑과 합)

즉 위의 3개는 문제의 조건에 부합하는 3개의 경우, 그 중 최솟값을 출력하면 된다.
"""
