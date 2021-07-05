perm = list(map(int, input().split()))

index = n-1

while index>0 and perm[index-1] >= perm[index]:
    index -= 1
if(index <= 0):
    print(-1)
"""
이 구간의 코드는 A[i-1] < A[i]가 되는 가장 큰 값인 i를 찾는 코드이다.
"가장 큰" i 값을 찾아야 하므로 for문이 아닌 while 문으로 제일 마지막까지 반복문을 돌리는 것이다.
index 값이 0보다 아래로 내려갔다는 것은, 최종 순열이라는 의미이므로 -1을 반환하도록 한다.
"""

jndex = index-1
while(jndex < n-1 and perm[jndex+1] > perm[index-1]):
    jndex += 1
"""
이 구간의 코드는 A[i-1] < A[j]가 되는 가장 큰 값인 j를 찾는 코드이다.
"가장 큰" j 값을 찾아야 하므로 똑같이 for문이 아닌 while 문으로 제일 마지막까지 반복문을 돌린다.
"""
perm[index-1], perm[jndex] = perm[jndex], perm[index-1]

jndex = n-1
while(index < jndex):
    perm[index], perm[jndex] = perm[jndex], perm[index]
    index += 1
    jndex -= 1
"""
마지막으로 i 이후의 순열을 완전히 뒤집어주는 코드이다.
"""
