sum = 0
max = 0

for i in range(0, 10):
    out, ride = map(int, input().split())
    sum = sum + ride - out
    if(sum > max):
        max = sum

print(max)

```
최근에 개발된 지능형 기차가 1번역(출발역)부터 10번역(종착역)까지 10개의 정차역이 있는 노선에서 운행되고 있다.
10개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.
```
