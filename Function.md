# Function
---
## Definition
```python
def functionName(par1, par2, ..):
  indented block of statements
  return expression
```
- 기본적으로 위와 같이 함수를 선언하고 이용한다.

## Function Manual
```python
help(print)
print(print.__doc__)
```
- __help()__ method나 __doc__ 을 이용하면, 함수를 어떻게 사용하는지 매뉴얼을 볼 수 있다.

## Local Variable & Global Variable
```python
def func(x):
  print('x is', x) // x is 50
  x = 2
  print('Changed local x to', x) // x to 2

func(x)
print('x is still', x) x is still 50
```
- x는 함수 func(x)의 Local variable이라서, 함수 내에서만 사용이 가능한 변수이다.
- 이를 함수 밖에서도 사용하려면 global varname 으로 선언을 해주어야 사용이 가능하다.
- global variable을 선언할 때에는, 다른 언어와 마찬가지로 대문자로 선언해주는 것이 좋다.
