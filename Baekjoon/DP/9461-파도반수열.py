import sys

case = int(sys.stdin.readline())
dp = [0]*101
dp[0], dp[1], dp[2], dp[3], dp[4], dp[5] = 0, 1, 1, 1, 2, 2

for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

for _ in range(case):
    num = int(sys.stdin.readline())

    print(dp[num])
  
"""
간단한 DP문제였다.
규칙만 찾으면 되는 것!
"""
