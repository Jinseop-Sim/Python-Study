# Greedy Algorithm(탐욕 알고리즘)
---
## Greedy?

> 그리디 알고리즘(탐욕 알고리즘)은 최적의 해를 구하는 경우에 사용되는 알고리즘이다.  
> 현 상황에서 가장 좋다고 판단되는 방향으로 해를 구해 나가는 알고리즘이기 때문에, 가장 좋은 결과를 보장하진 않는다.  

![캡처](https://user-images.githubusercontent.com/71700079/126977603-72b89c75-98b1-4a73-bd17-8b322aac05dc.PNG)  

- 위의 사진을 예로 들면, 그리디 알고리즘은 그 상황의 최적해를 구하는 것이므로, 7과 13중에 13을 고른다.  
- 그리고 그 이후 단계에서 5와 11중에 11을 골라 해를 24로 구할 것이다.  
- 하지만 그림을 보면 알 수 있듯이 문제 전체의 최적해는 107이 되어야 한다. 따라서 전체적인 최적해를 보장하지는 않는다.  

### Baekjoon 11047 : 동전
> 매우 간단한 그리디 알고리즘 연습 문제이다.  

![캡처](https://user-images.githubusercontent.com/71700079/126979975-aad6ee37-8d28-46c7-b664-276e1c22eaf5.PNG)  

```python
num, money = map(int, input().split())
cnt = 0
coin = []
for _ in range(num):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in coin:
    if money == 0:
        break
    cnt += money // i
    money %= i

print(cnt)

```
- 알고리즘의 생각 전개는 이러하다. 어쨌든 동전을 제일 적게 사용하고 K원을 만들어야 하므로, K원에 가장 가까운 제일 큰 돈부터 쓴다.  
- 예를 들어 K가 4200원이면, 1000원부터 사용을 하겠다는 말이다. 그러기 위해서는 내림차순으로 정렬을 하기 위해 reverse=True를 이용한다.  
- 반복문에 들어서면, 1000원보다 큰 나머지 금액은 money를 나누면 0이 되므로 cnt에 저장되지 않는다.  
- 그럼 1000원부터 4200 // 1000을 해서 cnt = 4, money는 4000원을 쓴 나머지 200  
- 그 다음으로 200을 나눌 수 있는 100원으로 나누어 200 // 100, cnt = 6이 된다.  
- 이 알고리즘이 그리디 알고리즘인 이유는 1000원을 만난 상황에서 최적해 4000원, 100원을 만난 상황에서 최적해 200원, 그리고 종료.  
- 4200원을 만들 수 있는 다른 경우는 전혀 생각을 하지 않기 때문에 그리디 알고리즘인 것이다.  

## 부록 : Priority Queue(우선순위 큐)
> 큐는 원래 FIFO(선입 선출)로 작동을 하지만, 우선순위 큐는 FIFO가 아닌 우선순위에 따라 삭제의 순서가 결정된다.  
> 큐나 스택은 O(1)의 시간 복잡도를 갖지만, 우선순위 큐는 O(logN)의 시간복잡도를 갖는다.  
> heapq 라는 모듈을 통해서 구현되어 있는 모듈이다. 즉 heap이 O(logN)의 시간복잡도를 가지므로, 우선순위 큐 또한 그렇다.  

```python
from queue import PriorityQueue # 이와 같이 모듈을 import한다.

queue = PriorityQueue() # 이와 같이 선언한다.
limitedqueue = PriorityQueue(maxsize=10) # 이는 크기가 제한된 우선순위 큐의 선언이다.

queue.put(1) # 이는 정수를 item으로 넣는 경우, 작은 정수부터 우선순위를 갖는다.
queue.put(2)

queue.put((1, 'Hello')) # 이는 tuple을 item으로 넣는 경우로, 우선순위를 매겨주어야 한다.
queue.put((2, 'World'))

queue.get() # 우선순위에 따라 item을 삭제하는 명령어
```

### Baekjoon 1715 : 카드 정렬하기  
> 매우 간단한 우선순위 큐를 사용해 풀 수 있는 문제이다.

![캡처](https://user-images.githubusercontent.com/71700079/127006070-400653ff-0429-4de8-81cd-1750bfd133a9.PNG)  

```python
import sys
from queue import PriorityQueue

num = int(sys.stdin.readline())
queue = PriorityQueue()
for i in range(num):
    queue.put(int(sys.stdin.readline()))

val = 0

while True:
    if(queue.qsize() == 1):
        break
    a = queue.get()
    b = queue.get()
    val += (a+b)
    queue.put(a+b)

print(val)
```
- 생각의 전개는 이러하다. 우리는 최소한의 비교를 만들어야 하기 때문에, 제일 작은 값끼리 먼저 더해 나가야 한다.
- 마치 그리디 알고리즘의 진행과 유사하다. 그러기 위해서 우선순위 큐에 집어 넣은다음, 그냥 두 정수를 get() 해주면, 알아서 제일 작은 두 값이 나온다.
- 그 둘을 더하고 다시 집어넣은 뒤, 또 두 정수를 get() 해서 더해주고 qsize() method를 이용해서 큐의 길이가 1이 되면 탈출하도록 한다.
