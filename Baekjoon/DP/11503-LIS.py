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
seq[3]보다 작은 수는 seq[0], seq[1], seq[2] 따라서 dp[3] = 

"""
