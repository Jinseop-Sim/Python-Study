case = int(input())

for i in range(case):
    num = int(input())
    stick = [list(map(int, input().split())) for _ in range(2)]

    stick[0][1] += stick[1][0]
    stick[1][1] += stick[0][0]

    for k in range(2, num):
        stick[0][k] += max(stick[1][k-1], stick[1][k-2])
        stick[1][k] += max(stick[0][k-1], stick[0][k-2])

    print(max(stick[0][num-1], stick[1][num-1]))
    
"""
DP 문제는 역시 수학적 사고력을 많이 요구하는 것 같다.
첫번째 인덱스에서 위쪽 아래쪽 두 개의 선택지가 존재한다.
위, 즉 [0][0] 선택 시 다음 선택지는 반드시 [1][1]이다.
아래, 즉 [1][0] 선택 시 다음 선택지는 반드시 [0][1]이다.

위 사실을 기반으로 최대값을 저장하며 앞으로 진행한다.

[0][0] -> [1][1] -> [0][3] or [0][2]
[1][0] -> [0][1] -> [1][3] or [1][2] 위와 같은 규칙을 갖고 계속 진행된다.

따라서 max 값 만을 계속 저장해서 오며, 최종적으로 더 큰 값을 출력하면 최대값이 된다.
"""
