"""
재귀함수를 이용해서 Fractal 모형을 출력하는 코드이다.
""" 

def starp(n):
    matrix = []
    for i in range(3*len(n)):
        if i // len(n) == 1:
            matrix.append(n[i%len(n)] + " " * len(n) + n[i%len(n)])
            """
            새로운 Matrix에다가 Star의 배열을 정해진 모양대로 append 하는 코드이다.
            i를 star의 길이로 나누었을 때, 소숫점을 뗀 몫이 1인 경우. i가 3일 때를 예로 들면, 3 4 5의 경우에
            가운데가 텅 빈 모양을 만들기 위한 코드이다.
            """
        else:
            matrix.append(n[i%len(n)]*3)
            """
            위의 조건이 아닐 때, 그냥 star을 정해진 모양대로 append하는 코드.
            """
    return(list(matrix))

star = ["***", "* *", "***"]
"""
기본 틀을 star이라는 List에 저장을 해놓는다.
"""

n = int(input())
k = 0
while n != 3:
    n = int(n/3)
    k += 1
    
for i in range(k):
    star = starp(star)
for i in star:
    print(i)
"""
n이 3일 때는, k값이 0이므로 반복문이 돌지 않아 그냥 star이 출력된다.
n이 3^i 일 때, k값이 i가 되므로, 반복문이 i번 돌면서 matrix가 재귀 호출에 의해서 계속 갱신된다.
"""

