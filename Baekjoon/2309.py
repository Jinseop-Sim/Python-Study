hei = []
sum = 0
key = 0

for i in range(0, 9):
    h = int(input())
    sum += h
    hei.append(h)

for j in range(0, 9):
    if(key == 100):
        break
    for k in range(j+1, 9):
        key = sum - (hei[j] + hei[k])
        if (key == 100):
            hei.remove(hei[j])
            hei.remove(hei[k-1])
            break

hei.sort()
for i in range(0, len(hei)):
    print(hei[i])

```
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다.  
일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.  
뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.  
아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.  
```
