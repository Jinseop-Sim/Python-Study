# Python's Array, LIST!
---
## List

## Tuple

## Dictionary
> Key와 Value를 통해 값을 정리해놓는 방식의 자료형이다.  
> 예컨대, {'Name : 홍길동', 'ID : 201724820'} 과 같은 형식으로 정리를 해놓는다.  
> 어떤 것의 정보를 저장하거나, 중요도를 매기는 등 다양한 곳에서 편리하게 쓰일 수 있다.  

- How to declare dictionary?
```python
dict = {'name' : 'hey', 'ID' : 201849230} # dictionary의 기본적인 선언 형태이다.
dict2 = {'a' : [1,2,3]} # 이렇게 Value에 List가 들어갈 수도 있다.
```
- How to use dictionary?
```python
dict = {'name' : 'Malon'}
dict['ID'] = 201524053 # 이런 식으로 Dictionary에 새 원소를 추가를 하거나 접근을 할 수 있다.

{'name' : 'Malon', 'ID' : '201524053'}

del dict['name'] # dictionary[key] 의 형태로 del 함수를 이용하면 원소 삭제 또한 가능하다.
```
- Dictionary Method
  - dict.keys()
  ```python
  dict = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
  dict.keys() # 이 함수를 출력해보면 dict_keys(['name', 'phone', 'birth']) 라는 Key만 모아놓은 배열이 추출된다.
  list(dict.keys()) # 이렇게 쓰게 되면, List로 변환하여 사용이 가능하다.
  ```
  - dict.values()
  ```python
  dict = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
  dict.values() # 물론 value의 List를 만드는 것 또한 가능하다. dict_values(['pey', '0119993323', '1118'])이 추출된다.
  ```
  - dict.items()
  ```python
  dict = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
  dict.items() # items() 함수는 Tuple 쌍으로 묶은 값을 배열로 추출해 준다. dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
  list(dict.items()) # 마찬가지로 List와 같이 사용이 가능하다.
  ```
  - dict.clear() : Dictionary를 싹 다 비워버린다.
 
- Caution!
  - Dictionary를 사용할 때, 중복되는 key 값이 존재하면 하나를 제외한 모두가 무시되므로 조심해야 한다.
  - Key에는 List가 들어갈 수 없다.
  - 물론 Value 값에는 무엇이든 들어갈 수 있다.
## Set
