def hanoi(num,a,b,c):
    if num == 1:
        print(a,c)
    else:
        hanoi(num-1,a,c,b)
        print(a,c)
        hanoi(num-1,b,a,c)

num = int(input())
sum = 1
for i in range(num-1):
    sum = sum*2 + 1
print(sum)
hanoi(num,1,2,3)

"""
간단한 재귀 문제인 하노이의 탑 문제이다.
하노이의 탑의 점화식은 2*(n-1) + 1. 그 이유는 n-1 단계를 2번 수행하고 제일 밑에 판만 마지막 칸으로 옮겨주면 되기 때문이다.
하지만 원래의 하노이의 탑은 a => c로 옮기는 것을 목적으로 a, b, c 순서로 인자를 줬지만
안의 재귀문에서는 a => b로 옮겨야 하므로 우선 a, c, b 순서로 인자를 주고(2번 자리를 3번 처럼 생각하고 판을 쌓도록)
마지막 판을 3번으로 옮긴 뒤에는, 2번째 판에서 3번째 판으로 옮겨야 하므로 b, a, c 순서로 인자를 준다.(2번자리를 1번처럼 생각하고 3번에 쌓도록)
"""
