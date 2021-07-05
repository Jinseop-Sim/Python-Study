init = eval(input())
num = init
i = 1

new = num // 10 + num % 10
num = (num % 10) * 10 + new % 10

while(num != init):
    new = num // 10 + num%10
    num = (num%10)*10 + new%10
    i += 1

print(i)

"""
덧셈의 싸이클 횟수를 저장하는 문제.
26 ==> 2+6=8 ==> 68
68 ==> 6+8=14 ==> 84
84 ==> 8+4=12 ==> 42
42 ==> 4+2=6 ==> 26

횟수는 4.
"""
