import sys

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x>20 or y>20 or z>20:
        return w(20, 20, 20)
    if dp[x][y][z]:
        return dp[x][y][z]
    if x < y < z:
        dp[x][y][z] = w(x, y, z-1) + w(x, y-1, z-1) - w(x, y-1, z)
        return dp[x][y][z]
    dp[x][y][z] = w(x-1, y, z) + w(x-1, y-1, z) + w(x-1, y, z-1) - w(x-1, y-1, z-1)
    return dp[x][y][z]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break

    print("w(%d, %d, %d) = %d"%(a,b,c,w(a,b,c)))

"""
DP를 이용한 메모이제이션의 정확한 예시를 들어주는 문제이다.

어차피 20을 넘으면 20으로 초기화 시켜주고, 0 이하로 내려가면 1로 초기화 시켜주므로
dp[] 배열의 칸을 20칸씩 3차원으로 만들어주면 된다. 변수가 a, b, c 3개 이므로 3차원이다.

그 이후 w 함수를 동일하게 연산 시켜주는데, 재귀 함수와 다른 점은?
재귀 함수는 매번 연산을 해주어야 하지만, 메모이제이션은 dp 배열에 모든 값을 저장하므로 그 때 그 때 꺼내서 쓸 수가 있다.
따라서 연산의 속도가 빠르다!
"""
