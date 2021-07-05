n = int(input())
pibo = [0,1]

for i in range(0, n):
    pibo.append(pibo[i]+pibo[i+1])
    
print(pibo[n])

```
간단한 피보나치 수열 문제이다.
```
