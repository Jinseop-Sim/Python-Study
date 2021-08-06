import sys

num = int(sys.stdin.readline())
seq = list(map(int, input().split()))
dp = [0]*num

for i in range(num):
    for j in range(i):
        if seq[i] < seq[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1


print(max(dp))

"""
전형적인 DP문제의 두 번째 LDS(가장 긴 감소하는 부분수열)이다.

LIS와 같은 방식이지만 seq[i] < seq[j]로 조건만 바꾸어주면 끝난다.
"""
