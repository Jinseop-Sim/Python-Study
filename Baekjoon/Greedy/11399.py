num = int(input())
time = list(map(int, input().split()))
time.sort()

for i in range(1, num):
    time[i] += time[i-1]

print(sum(time))

"""
간단한 Greedy 문제이다.
Python에는 sum()이라는 아주 유용한 내장함수가 존재한다.
"""
