m = int(input())
n = int(input())
sum = 0
min = 10001

for i in range(m, n+1):
    for j in range(2, i+1):
        if(j == i):
            sum += i
            if(min > i):
                min = i
        elif(i%j == 0):
            break

if(sum == 0):
    print(-1)
else:
    print(sum)
    print(min)
    
```
소수 찾기 문제의 응용 문제이다.
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성한다.
```
