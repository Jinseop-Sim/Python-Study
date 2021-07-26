num, money = map(int, input().split())
cnt = 0
coin = []
for _ in range(num):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in coin:
    if money == 0:
        break
    cnt += money // i
    money %= i

print(cnt)

"""
간단한 그리디 알고리즘 기초 문제이다.
"""
