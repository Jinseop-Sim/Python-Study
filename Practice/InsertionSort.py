ins = list(map(int, input().split()))

for i in range(1, len(ins)):
    key = ins[i]
    j = i-1
    while j>=0 and ins[j] > key:
        ins[j+1] = ins[j]
        j -= 1
    ins[j+1] = key

print(ins)

```
O(N^2)의 시간복잡도를 가지는, 삽입 정렬 알고리즘이다.
```
