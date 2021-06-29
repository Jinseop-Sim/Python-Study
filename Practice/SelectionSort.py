select = list(map(int, input().split()))
for i in range(0, len(select)):
    min = i;
    for j in range(i+1, len(select)):
        if(select[j] < select[min]):
            min = j
            
    temp = select[i]
    select[i] = select[min]
    select[min] = temp

print(select)

```
선택 정렬 알고리즘 연습 코드 입니다.
