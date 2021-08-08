import sys

num = int(sys.stdin.readline())
pillar = []
dp = [0]*num

for _ in range(num):
    pillar.append(list(map(int, input().split())))
pillar.sort()

for i in range(num):
    for j in range(i):
        if pillar[i][1] > pillar[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(num-max(dp))

"""
LIS의 응용 문제이다.

전깃줄 앞 뒤 번호를 각각 a, b라고 할 때
a를 오름차순으로 정렬을 해놓으면 이제 b 또한 오름차순이 되어야 교차가 발생하지 않는다는 얘기이다.
따라서 몇 개를 잘라야 할까의 문제는 전체 갯수에서 LIS의 길이를 빼주면 된다.
"""
