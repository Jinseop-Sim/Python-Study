# Input/Output & Variable
---
## How to Input?
```python
a = input()
```
Python은 기본적으로 input() 함수를 이용하여, 입력을 받을 수 있다.  
하지만 이는 문자열만 입력을 받는 함수이기 때문에 공백 또한 문자열에 집어 넣어버린다.  
즉, Enter 키의 입력으로만 다음 입력을 받을 수 있다.  

하지만, 정수 입력을 받거나 특정 상황에는 불편함을 느낄 수가 있다.  
```python
a = input().split()
b, c = map(int, input().split())
```
그런 경우에는, 위와 같은 split()함수를 이용하면 공백을 기준으로 잘라서 입력을 받게 된다.
아래의 b는 map() 함수를 이용해서 정수 값 여러개를 동시에 입력받는 가장 흔한 형태의 코드이다.

## How to Output?
```python
print("Hello World")
```
파이썬은 C언어와는 달리 그냥 print() 함수를 이용해서 출력이 가능하다.  

## How to Declare Variable?
```python
a = 1000
b = 200
```
파이썬은 C언어와는 달리 변수의 선언이 따로 필요가 없이 바로 Initialize가 가능하다.  
각 줄의 끝에 세미콜론도 따로 붙이지 않는다.

### String Variable
```python
print("=" * 50)
a = "Hello World"
b = " My Darling"
c = "I said, \" Hello World\" "
print(a+b)
print("=" * 50) 
```
파이썬에서의 문자열은 위와 같이 변수 초기화가 가능하다.  
그리고 신경을 써줘야 할 부분은 문자열 내에 따옴표가 넣고 싶으면, 백슬래쉬(\)를 이용해서 넣어주어야 한다는 점.  
그렇지 않으면 Syntax Error이 발생한다.   
그리고 파이썬의 특이한 점은, 문자열끼리 덧셈을 하게 되면 문자열이 서로 연결이 가능하다는 점이다.  
또한 곱셈을 하게 되면 그 문자열을 특정 횟수 반복 출력하게 된다.
