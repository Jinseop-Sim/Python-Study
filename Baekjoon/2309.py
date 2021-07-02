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
