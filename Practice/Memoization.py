n = int(input())
memo = [0, 1]

for i in range(2, n+1):
    memo.append(memo[i-1] + memo[i-2])

print(memo[n])

"""
피보나치의 메모이제이션 구현(DP)
"""
