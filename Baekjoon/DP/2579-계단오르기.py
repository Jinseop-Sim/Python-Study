import sys

num = int(sys.stdin.readline())
stair = [0]*301
dp = [0]*301
for i in range(num):
    stair[i] = int(sys.stdin.readline())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])
for i in range(3, num):
    dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i]+stair[i-1])

print(dp[num-1])

"""
DP 문제, 포도주 시식과 유사한 문제이다.
모든 경우의 수를 적어보며 저장, 이전 값들과 비교하여 연산.
"""
