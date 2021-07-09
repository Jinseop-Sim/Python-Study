n = int(input())

dp = [1, 2]

for i in range(2, n):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n-1]%10007)

"""
아주 간단한 DP문제이다.
문제의 규칙이 매우 간단해 점화식을 찾기 쉬웠다.
"""
