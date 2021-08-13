import sys

num = int(sys.stdin.readline())
ser = list(map(int, sys.stdin.readline().split()))
sum = [ser[0]]

for i in range(len(ser)-1):
    sum.append(max(sum[i] + ser[i+1], ser[i+1]))

print(max(sum))

"""
현재 sum list의 값과 다음 ser 값을 더한게 크다면, 그걸 sum에 append하고
크지 않다면, 다음 ser 값을 그냥 sum에 append 시킨다.
이런식으로 큰 값만 저장해서 더하면, 최대값이 나온다.
"""
