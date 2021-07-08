n = int(input())
cnt = 0
sum = 1
i = 2

while sum:
    if (sum > n):
        break
    sum = sum+i
    cnt += 1
    i += 1

print(cnt)

"""
수의 합 S가 입력으로 주어질 때
S를 만들기 위한 자연수의 최대 갯수를 출력하는 코드이다.
"""
