ins = list(map(int, input().split()))

for i in range(1, len(ins)):
    key = ins[i]
    for j in range(0, len(ins)):
        if(key < ins[j]):
            ins[i], ins[j] = ins[j], ins[i]

print(ins)

```
O(N^2)의 시간복잡도를 가지는, 삽입 정렬 알고리즘이다.
굳이 key 변수를 따로 만들 필요는 없지만, 가독성을 위해 만들었다.
```
