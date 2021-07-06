def fact(num):
    sum = 1
    if(num == 1):
        return 1

    return num * fact(num-1)

n = int(input())

print(fact(n))

"""
반복문으로 만들 수 있는 팩토리얼을 재귀 호출을 이용해서 만든다.
"""
