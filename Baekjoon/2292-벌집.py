import sys

num = int(sys.stdin.readline())

comb = 1
cnt = 1
while num > comb:
    comb += 6*cnt
    cnt += 1

print(cnt)

"""
벌집의 구조상 한 층 지날 때 마다 6개씩 방이 늘어난다.

따라서 입력받은 num을 넘지 않는 선의 comb에서 반복문이 몇 회 돌았는지 세어주면 된다.
comb += 6*cnt 로 하게 되면, comb는 +6, +12, +18 로 증가하게 된다.
"""
