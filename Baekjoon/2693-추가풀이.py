case = int(input())

for i in range(0, case):
    val = list(map(int, input().split()))
    val.sort()
    print(val[len(val)-3])
    
```
내림차순 정렬을 한 다음, 뒤에서 세 번째 값이 세 번째로 큰 값이 됨을 간단하게 알 수 있다.
```
