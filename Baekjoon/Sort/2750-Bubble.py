n = int(input())
sort = []

for a in range(0, n):
    elem = int(input())
    sort.append(elem)

for i in range(0, n):
    for j in range(i+1, n):
        if(sort[i] > sort[j]):
            temp = sort[i]
            sort[i] = sort[j]
            sort[j] = temp

for k in range(0, n):
    print(sort[k])
    
```
2750번 문제, 간단한 수 정렬하기 문제이다.
정렬 알고리즘을 실습하기 위해 풀어보았다.
가장 단순한 복잡도(N^2)의 정렬인 버블 정렬이다.
```
