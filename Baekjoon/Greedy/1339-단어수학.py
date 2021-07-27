import sys

num = int(sys.stdin.readline())
word = []

for _ in range(num):
    word.append(list(input()))

alpha_dict = {} # Dictionary의 선언은 {}, 중괄호로!

for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j] not in alpha_dict: # 최초의 alpha_dict는 비어있는 상태이다. 따라서 원소들을 하나하나 추가해준다.
            alpha_dict[word[i][j]] = pow(10, len(word[i])-j-1) # alpha_dict[알파벳] = 값 으로 저장을 하면, 알파벳 : 값 식으로 저장이 된다.
                                                               # len(word[i]) 는 총 몇 자리 수 인지, j를 빼는 것은 몇 째 자리에 위치하는지, 10^n을 하는 것이므로 1을 뺀다.
        else: # dict에 이미 있는 중복되는 알파벳이 있다면, 중요도를 높여주기 위해서 한번 더 더해준다.
            alpha_dict[word[i][j]] += pow(10, len(word[i])-j-1)

alpha_list = sorted(alpha_dict.items(), key=lambda x:x[1], reverse=True) # alpha_dict.items() method로 내부 원소 순회가 가능하다. 값을 기준으로 내림차순 정리.
result = 0
num = 9

for i in range(len(alpha_list)):
    result += alpha_list[i][1]*num # 중요한 알파벳 부터 9, 8, 7 .. 순서대로 곱하며 결과값에 더해준다.
    num -= 1

print(result)

"""
굉장히 고난이도의 Greedy 문제였다.

1. Dictionary의 사용법을 제대로 익힌다.
2. 어떤 상황에서 Dictionary를 사용할 지 생각해본다.
"""
