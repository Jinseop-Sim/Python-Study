import sys

case = int(sys.stdin.readline())
sum = [0]*10000001

for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        sum[j] += i
    sum[i] += sum[i-1]

for _ in range(case):
    print("{}\n".format(sum[int(sys.stdin.readline())]))
    
"""
1부터 x까지 약수의 합을 f(x) 라고 할 때
1부터 N까지의 f(x)들의 합을 g(N)이라고 하겠다.
원하는 g(N)을 출력하라.

그냥 반복문만을 돌리는 간단한 알고리즘을 사용한다면, 1,000,000 까지 모두 연산해야 하는 경우 천문적인 시간이 걸린다.
따라서 배열에 저장을 하는 방법을 이용하자.

for j in range(i, 1000001, i) 의 코드를 적어 놓으면, sum[j]번째는 i를 약수로 갖는 수들만 오게 된다. 따라서 i를 그 자리에 누적해주면 되는 것.
위의 합 까지는 f(x)만 1~1000001 까지 구해놓은 것.

그럼 이제 sum[i] += sum[i-1]로 f(x)들을 누적합 시켜주면, g(N)이 구해지는 것!
"""
