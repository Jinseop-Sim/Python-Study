case = int(input())
num = []
for i in range(0, case):
    num.append(int(input()))

for i in range(0, case):
    index = 0
    while num[i] != 0:
        if(num[i]%2 == 1):
            print(index)
            index += 1
            num[i] = num[i] // 2
        elif(num[i]%2 == 0):
            index += 1
            num[i] = num[i] // 2
            
```
양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오.  
최하위 비트(least significant bit, lsb)의 위치는 0이다.  
간단한 이진수 변환 문제였다.
```
