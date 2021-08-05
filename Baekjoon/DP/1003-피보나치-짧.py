import sys

case = int(sys.stdin.readline())
for _ in range(case):
    dp = [0, 1]
    zero = [1, 0]
    num = int(sys.stdin.readline())
    for i in range(2, 41):
        dp.append(dp[i-1] + dp[i-2])
    if num == 0:
        print(*zero)
    else:
        print(dp[num-1], dp[num])
      
"""
메모이제이션을 이용하여 함수 없이 만든 더 짧은 풀이이다.
"""
