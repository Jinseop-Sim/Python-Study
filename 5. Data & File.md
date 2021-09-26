# Data Processing & Reading File
---
## Reading File
```python
def displayWithForLoop(file):
  infile = open(file, 'r')
  for line in infile:
    print(line.rstrip()
  infile.close()

def displayWithListComprehension(file): # 위와 같이 한 줄 씩 읽은 후, List에 저장하는 함수 구현
  infile = open(file, 'r')
  listPres = [line.rstrip() for line in infile]
  infile.close()
  print(listPres)

file = "FirstPresidents.txt"
displayWithForLoop(file)
print()
displayWithListComprehension(file)
```
- 위의 코드와 같이 open() 메서드를 이용해 권한을 'r'로 설정하여 파일을 읽어올 수 있다.
- 물론 같은 폴더 내에 파일이 존재해야 읽어올 수 있다.
- for line in infile을 이용해서 한 줄씩 받아온다.
- 항상 close() 메서드로 파일을 닫아주어야 한다!

### Creating Text Files
```python
def createWithWrite(L, outfile):
  for i in range(len(L)):
    outfile.write(L[i] + "\n")
  outfile.close()

L = ["George", "Adams", "Jefferson"]
outfile = open("FirstPresidents2.txt", 'w')
createWithWrite(L, outfile)
```
- open() 메서드 내의 권한을 'w', 즉 Write로 설정을 해서 파일을 만든다.
- 마찬가지로 close() 메서드로 닫아주어야한다.
- write 권한으로 파일을 실행시킬 경우, 초기화가 되므로 중요한 정보를 날리지 않도록 조심해야 한다.
- 반드시 매개변수로 입력을 넣을 List와 File을 넘겨주어야 한다.

```python
def createListFromFile(fileName):
  infile = open(fileName, 'r')
  desiredList = [line.rstrip() for line in infile]
  infile.close()
  return desiredList
  
def createNewFile(listName, oldFileName, newFileName):
  infile = open(oldFileName, 'r')
  outfile = open(newFileName, 'w')
  for person in infile:
    if person.rstrip() in listName:
      outfile.write(person)
  infile.close()
  outfile.close()
  
  vicePresList = createListFromFile("VPres.txt")
  createNewFile(vicePresList, "USPres.txt", "Both.txt")
  ```
  - 위의 코드는 파일로 입력을 받아서, 출력 파일을 만드는 코드이다.

### Adding Lines to Files
```python
outfile = open("FirstPresidents.txt", 'a')
list1 = ["Madison\n", "Monroe\n"]
outfile.writelines(list1)
outfile.write("John Q\n")
outfile.close()
```
- Append를 시킬 경우, 'a'의 권한으로 파일을 열어야한다.
- 사용되는 메서드는 write 권한의 메서드와 동일하지만 둘의 차이는 write 권한은 아예 초기화를 시키고 새로 쓴다는 것이다.
- 하지만 'a' 권한은 이미 있는 내용에 append만 시키는 것이라 초기화되지 않는다.

### Altering Items in Files
```python
import os

os.remove(filenName) # 원하는 파일을 지우는 method
os.rename(oldFileName, newFileName) # 원하는 파일의 이름을 바꾸는 method
os.path.isfile(fileName) # 원하는 파일이 해당경로 내에 있는지 확인하는 method, boolean type을 return한다.

if os.path.isfile("ABC.txt"): # 해당 경로내에 ABC.txt가 없다면, 새로 생성하는 코드.
  print("File already exists.")
else:
  infile = open("ABC.txt", 'w')
  infile.write("a\nb\nc\n")
  infile.close()
```
- os 패키지를 import해서 다양한 위와 같은 메서드들을 이용할 수 있다.
