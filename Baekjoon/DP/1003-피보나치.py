import sys

def fibo(n):
    if n == 0:
        dp[0] = 0
        return 0
    if n == 1:
        dp[1] = 1
        return 1
    if dp[n]:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

case = int(sys.stdin.readline())
for _ in range(case):
    dp = [0]*41
    zero = [1, 0]
    num = int(sys.stdin.readline())
    fibo(num)
    if num == 0:
        print(*zero)
    else:
        print(dp[num-1], dp[num])

"""
0 = 0
1 = 1
2 = 0 + 1
3 = 1 + (0+1)
4 = (0+1) + (1 + 0 + 1)
5 = (0 + 1 + 1 + 0 + 1) + (1 + 0 + 1)

이런 식으로 진행 되므로, 어차피 n번째 피보나치 수와, n-1번째 피보나치 수를 출력하면 그 0과 1의 갯수와 동일해진다.
"""
