import sys

num = int(sys.stdin.readline())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3, num+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[num])

"""
DP문제 - 점화식 문제였다.
피보나치의 Memoization
"""
