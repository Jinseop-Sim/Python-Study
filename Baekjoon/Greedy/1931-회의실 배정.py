import sys

num = int(sys.stdin.readline())
room = []
cnt = 1
for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())
    room.append([a, b])
room.sort()
room.sort(key = lambda x:x[1])

end = room[0][1]

for i in range(1, num):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)

"""
쉬운 그리디 문제였다.
정보의 정렬을 어떻게 할 것인가가 관건이었다.

1. 회의가 빨리 끝나는 회의가 많을 수록, 겹치지 않고 강의실을 많이 사용할 수 있을 것이다.
2. 따라서 회의를 끝나는 시간 오름차순으로 정렬을 하는데, 이 때 끝나는 시간이 같은 경우 시작시간이 더 빠른 회의가 먼저 들어가야 하므로,
3. 시작시간 오름차순으로 정렬을 한 뒤 ==> 끝나는 시간 오름차순 정렬을 해주면 시작시간이 더 빠른 회의가 앞으로 온다.
4. 그 후에 회의 시간이 겹치지 않는 회의만 Count 해주면, Greedy 방식을 이용한 풀이가 끝난다.
"""
