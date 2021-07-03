case = int(input())
val = []

for i in range(0, case):
    max = 0
    smax = 0
    tmax = 0
    arr = list(map(int, input().split()))
    for j in range(0, len(arr)):
        if(max < arr[j]):
            max = arr[j]
    for k in range(0, len(arr)):
        if(smax < arr[k] < max):
            smax = arr[k]
    for t in range(0, len(arr)):
        if(tmax < arr[t] < smax):
            tmax = arr[t]

    val.append(tmax)

for i in range(0, case):
    print(val[i])
    
```
간단한 3번째로 큰 수 구하기 문제이다.
그러나 코드가 너무 지저분해서 더 짧게 하는 법을 공부해야한다.
```
