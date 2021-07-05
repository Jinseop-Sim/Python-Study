num = int(input())
val = list(map(int, input().split()))

max = -1000000
min = 1000000

for i in range(0, len(val)):
    if(min > val[i]):
        min = val[i]
    if(max < val[i]):
        max = val[i]

print(min, max)

```
가장 간단한 최소 최대 값을 구하는 문제이다.
```
