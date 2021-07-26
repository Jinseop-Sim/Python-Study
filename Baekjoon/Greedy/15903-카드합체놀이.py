num, m = map(int, input().split())
card = list(map(int, input().split()))
temp = 0

for _ in range(m):
    card.sort()
    temp = card[0] + card[1]
    card[0] = temp
    card[1] = temp

print(sum(card))

"""
매우 간단한 그리디 알고리즘이다.
합체를 할 때 마다 최솟값을 만들어주면 되므로, 그리디 알고리즘이다.
"""
