import sys

n, k = map(int, sys.stdin.readline().split())
bag = [[0,0]]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    bag.append(list(map(int, input().split())))

print(bag)

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = bag[i][0]
        value = bag[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[n][k])

"""
문제의 "무게 K를 넘지 않으며 Value가 최대가 되게 하라" 가 핵심이다.

1. dp[n][k] 배열을 만들 것인데, 이는 N번째 물건까지 보았을 때, 무게가 K인 배낭의 최대 Value를 의미한다.
2. 물건에 배낭을 담을 때, 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면, Value = 0.
3. 현재 배낭의 허용 무게보다 넣을 물건의 무게가 작다면, 다시 두 가지로 갈린다.
  - 현재 넣을 물건의 무게만큼 배낭에서 빼고 현재 물건을 다시 넣는다. ==> value + dp[i-1][j-weight]
  - 현재 물건을 넣지 않고 이전 배낭 그대로 가지고 간다. ==> dp[i-1][j]
  - 둘 중 더 가치있는 쪽을 택하는 것.
4. dp[n][k]를 출력하면, 무게 K를 넘지 않는 최대 Value가 된다.
"""
