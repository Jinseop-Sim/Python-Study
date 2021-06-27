# Control Flow
---
## If(Conditional)
```python
if(num!=0):
  print("it's not Zero")
else:
  print("It's Zero")
```

Python의 if문은 위와 같은 기본 Indent와 문법을 갖는다.  
또한 C언어에는 없는 elif(else if)가 사용이 가능하다.  

```python
if(num%2 == 0 and num > 0):
  print("It's Even")
elif(num%2 != 0 and num > 0):
  print("It's odd")
else:
  print("It's not Natural Number")
```

위와 같이 elif가 사용이 가능하며, and or not 과 같은 논리적 조건을 사용할 때에는  
&&, ||와 같은 기호가 아닌 영어로 적어 사용한다.  

## For & While(Iteration)

### While
```python
hit = 0
while(hit<10):
  hit += 1
  print("Hit count : %d!" %hit)
  if(hit == 10):
    print("Tree is Dead")
 ```
 
 위와 같은 형태를 기본으로 while문을 사용한다.  
 아래와 같이 메뉴의 형태로 이용도 가능하다.  
 
 ```python
message = """
1. Add
2. Del
3. List
4. Quit

Enter Number : 
"""

num = 0
while num != 4:
    print(message)
    num = eval(input())

print("Good bye!")
```

또는 아래와 같이 if문 내의 break를 이용한 응용도 가능하다.  
while문을 강제 종료 시키는 것이다.

```python
money = 5000
coke = 5 
while money:
  print("Coke is 1000 dollars!")
  coke -= 1
  print("Rest coke is %d" %coke)
  if(coke==0):
    print("SOLD OUT")
    break;
```

### For
```python
points = [90, 80, 45, 75, 80]
number = 0

for i in points:
    number += 1
    if i >= 80:
        print("Student %d is PASS"%number)
    else:
        print("Student %d is FAIL"%number)
```

대표적으로 위와 같은 for문을 사용할 수 있다.  
list points 내의 점수들을 i에 가져와서 하나씩 비교를 하는 형식이다.  
C언어와는 다른 형태로 사용되는 것이다.  

```python
points = [90, 80, 45, 75, 80]
number = 0

for i in points:
    number += 1
    if i < 80:
        continue
    print("Student %d is PASS"%number)
```
위와 같이 if문 내의 continue와 함께 사용해서 합격한 학생만 출력되도록 하는 것도 가능하다.  

```python
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = " ")
    print('')
    
sum = 0
for i in range(1,101):
    sum += i

print(sum)
```
그리고 for문과 같이 대표적으로 사용될 수 있는 함수가 바로 range() 함수이다.  
for 문 안에서 사용될 iterator의 범위를 지정해서 사용하도록 하는 함수이며  
위는 range 함수의 예를 가장 잘 표현한 구구단과 1부터 100까지의 합 코드이다.  
