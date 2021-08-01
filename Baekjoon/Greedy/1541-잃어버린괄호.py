strin = list(input().split('-'))
num = []

for i in strin:
    sol = 0
    part = i.split('+')
    for j in part:
        sol += int(j)
    num.append(sol)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]

print(n)

"""
문자열 파싱에 대해서 깨달음을 얻어간 중요한 문제이다.
"""
