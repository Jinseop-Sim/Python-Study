n, m = map(int, input().split())
card = list(map(int, input().split()))

sum = 0
max = 0
for i in range(0, len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            sum = card[i] + card[j] + card[k]
            if(max < sum <= m):
                max = sum

print(max)

```
2798번 문제, 블랙잭 문제이다.
Brute Force 형식으로 모든 값들을 다 더해보고
정해진 m 값에 가장 근접한 합을 찾아 내는 코드이다.
```
