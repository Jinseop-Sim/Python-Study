n = int(input())
perm = list(map(int, input().split()))

cnt = 0
index = n-1

while index>0 and perm[index-1] >= perm[index]:
    index -= 1
if(index <= 0):
    print(-1)
    cnt += 1

jndex = index-1
while(jndex < n-1 and perm[jndex+1] > perm[index-1]):
    jndex += 1

perm[index-1], perm[jndex] = perm[jndex], perm[index-1]

jndex = n-1
while(index < jndex):
    perm[index], perm[jndex] = perm[jndex], perm[index]
    index += 1
    jndex -= 1

if(cnt != 1):
    for i in range(0, n):
        print(perm[i])
        
"""
내가 적은 순열 다음으로 올 순열을 만드는 코드이다.
Python에는 itertools 내에 순열 함수가 있지만, 완전 탐색에 대한 공부를 위해 직접 짰다.
"""
