import sys

num = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
sum = 0

card.sort(reverse=True)

sum += card[0]*(len(card)-1)
for i in range(1, len(card)):
    sum += card[i]

print(sum)

"""
되게 간단한 Greedy 문제였는데, 수학적 사고력이 부족했던 것 같다.
어차피 가장 큰 숫자를 기준으로 주변 숫자들을 합치게 될 것이다.
그럼 결국 레벨이 가장 높은 숫자만 남는 것이고, 어차피 그 숫자는 계속 더해진다.

따라서 (레벨이 가장 높은 카드 * (N-1)) + 나머지 카드 레벨을 해주면 정답이다.
"""
