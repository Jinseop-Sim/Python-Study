from itertools import combinations

n, m = map(int, input().split(" "))
l = list(map(int, input().split(" ")))

max = 0

for c in combinations(l, 3):
    temp=sum(c)
    if max < temp <= m:
        max = temp

print(v)

```
2798번 블랙잭 문제의 추가풀이이다.
Python 내의 itertools라는 모듈에는 Combinations라는 조합 메서드가 존재한다.
이는 list와 정수 값을 인자로 받아 lC3 의 조합을 구현해주는 메서드이다.
이를 이용하면 매우 간단하게 구할 수가 있다.
```
