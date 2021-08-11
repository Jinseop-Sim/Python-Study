num, k = map(int, input().split())
div = []

for i in range(1,num+1):
    if(num%i==0):
        div.append(i)
if(k > len(div)):
    print(0)
else:
    print(div[k-1])
    
```
간단한 약수 구하기 문제이다.
num으로 받은 약수들 중 k번째로 작은 약수를 출력하는 문제.
k보다 약수의 갯수가 작으면 0을 출력한다.
```
