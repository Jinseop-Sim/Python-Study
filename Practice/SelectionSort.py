select = list(map(int, input().split()))
for i in range(0, len(select)):
    min = i;
    for j in range(i+1, len(select)):
        if(select[j] < select[min]):
            min = j

    select[i], select[min] = select[min], select[i]

print(select)

```
선택 정렬 알고리즘 연습 코드 입니다.
파이썬은 타 언어와는 다르게 Swap 기능을 제공합니다.
list[0], list[1] = list[1], list[0] 의 형태로 제공합니다.
```
