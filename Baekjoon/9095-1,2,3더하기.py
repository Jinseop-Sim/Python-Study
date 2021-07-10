case = int(input())
dp = [1, 2, 4]

for i in range(0, case):
    dp = [1, 2, 4]
    n = int(input())
    for j in range(3, n):
        dp.append(dp[j-3]+dp[j-2]+dp[j-1])
    print(dp[n-1])
    
"""
매우 간단한 DP 문제이다.
1 = 1
2 = (1+1), 2
3 = (1+1+1), (1+2), (2+1), 3
4 = (1+1+1+1), (1+2+1), (2+1+1), (3+1) (dp[1]) | (1+1+2), (2+2) (dp[2]) | (1+3) (dp[3])

이런 식으로 진행됨을 쉽게 알 수 있다.
따라서 점화식은 dp[i] = dp[i-3] + dp[i-2] + dp[i-1] 이다.
"""
