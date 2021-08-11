import sys

money = int(sys.stdin.readline())
charge = 1000 - money
mon = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in mon:
    if i <= charge:
        cnt += charge // i
        charge %= i
    if charge == 0:
        break

print(cnt)

"""
간단한 Greedy 알고리즘 이다.
"""
