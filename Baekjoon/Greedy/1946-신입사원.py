import sys
from collections import deque

case = int(sys.stdin.readline())
for _ in range(case):
    num = int(sys.stdin.readline())
    man = []
    cnt = 1
    for i in range(num):
        a, b = map(int, sys.stdin.readline().split())
        man.append([a, b])

    man.sort()
    max = man[0][1]

    for i in range(1, num):
        if max > man[i][1]:
            cnt += 1
            max = man[i][1]

    print(cnt)

"""
왜 Greedy 문제인가?

서류 순위를 기준으로 오름차순으로 정리를 해놓으면, 당연히 서류 순위 1위는 무조건 합격.
그 이후로 서류 순위 1위의 면접 순위보다 낮은 면접 순위를 가진 사람들은 당연히 탈락!
하지만 서류 순위 1위를 제외한 다른 면접자에 때문에 떨어지는 경우가 있을 수도 있으므로, max 값을 다음 합격자의 면접 순위로 바꾸어 준다.
"""
