a, b = map(int, input().split())

per = []
sum = 0

for i in range(1, 46):
    val = i
    for j in range(0, i):
        per.append(val)

for k in range(a, b+1):
    sum += per[k-1]

print(sum)

```
간단한 수열 만들기 문제이다.
수열을 배열에 저장한 뒤, 원하는 구간의 합을 구했다.
```
