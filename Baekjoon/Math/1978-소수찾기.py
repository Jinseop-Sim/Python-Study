case = int(input())
num = list(map(int, input().split()))
cnt = 0

for i in range(0, case):
    for j in range(2, num[i]+1):
        if (j == num[i]):
            cnt += 1
        elif(num[i]%j==0):
            break

print(cnt)
```
간단한 소수 찾기 문제이다.
2부터 자기 자신 까지 나눠보는 방법을 채택했다.
물론 소수를 판별하는 방법에는

1. Deterministic Test
2. Fermat Test
3. Deterministc + Miller-Rabin Test

의 세 가지가 존재하는데, 아직 위의 방법을 코드로 구현하기에는 실력이 부족하다.
```
