case = int(input())

for i in range(0, case):
    val = list(map(int, input().split()))

    for j in range(0, len(val)):
        minindex = j
        for k in range(j+1, len(val)):
            if(val[k] < val[minindex]):
                minindex = k

        val[j], val[minindex] = val[minindex], val[j]
    print(val[len(val)-3])
    
```
내림차순 정렬을 한 다음, 뒤에서 세 번째 값이 세 번째로 큰 값이 됨을 간단하게 알 수 있다.
선택정렬을 사용하였다.
```
