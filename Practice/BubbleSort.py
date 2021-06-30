n = int(input())
sort = []

for a in range(0, n):
    elem = int(input())
    sort.append(elem)

for i in range(0, n):
    for j in range(i+1, n):
        if(sort[i] > sort[j]):
            sort[i], sort[j] = sort[j], sort[i]

for k in range(0, n):
    print(sort[k])
