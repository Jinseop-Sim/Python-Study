a, b = map(int, input().split())
big = 0
small = 0
rem = 0
gcd = 0
lcm = 0

if(a>b):
    big = a
    small = b
else:
    big = b
    small = a

rem = big%small
while(rem != 0):
    big = small
    small = rem
    rem = big%small

gcd = small

lcm = (a*b)//gcd

print(gcd)
print(lcm)

```
수학 알고리즘의 기초가 되는 최대공약수 / 최소공배수 구하기 문제이다.
유클리드 호제법을 이용하여 알고리즘을 작성한다.
```
