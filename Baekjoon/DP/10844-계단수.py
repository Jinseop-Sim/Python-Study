leng = int(input())

dp = [[0 for i in range(10)]for j in range(leng+1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2, leng+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]

print(sum(dp[leng])%1000000000)

"""
DP 문제를 풀 때, 1차원 배열만이 아닌 2차원 배열으로도 문제를 풀 수 있다는 것을 인지하라.
dp[자릿 수][맨 끝자리 수]로 표를 만들어 보면 특정한 규칙을 가졌음을 알 수 있다.
"""
