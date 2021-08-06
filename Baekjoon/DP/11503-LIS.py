import sys

num = int(sys.stdin.readline())
seq = list(map(int, input().split()))
dp = [0]*num

for i in range(num):
    for j in range(i):
        if seq[i] > seq[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1


print(dp)

"""
DP의 전형적인 문제인 LIS(가장 긴 증가하는 부분수열) 문제 이다.

seq 10 20 10 30 20 50
dp  0  0  0  0  0  0  이라고 가정할 때

seq[0]보다 작은 수는 배열에 없다. dp[0] = 1
seq[1]보다 작은 수는 seq[0], 따라서 dp[1] = dp[0]+1 = 2
seq[2]보다 작은 수는 없다. 따라서 dp[2] = 1
seq[3]보다 작은 수는 seq[0], seq[1], seq[2] 따라서 dp[3] = dp[1] + 1 = 3 (why? dp[i]가 dp[j] 보다 작으면 바꾸지 않는다. 그래서 2에서 멈춘 채로 돈다.)

위와 같은 방식으로 계속 해 나가면, seq[5]인 50보다 작은 수열은 4개가 된다. 왜냐하면 dp[i] < dp[j] 의 조건에서 dp[5] = dp[3] + 1 = 4 가 될 것이다.
따라서 가장 긴 부분 수열의 길이는 4!
"""
