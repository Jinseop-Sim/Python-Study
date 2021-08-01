word = list(input())
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(alpha)):
    for j in range(len(word)):
        if alpha[i] == word[j]:
            alpha[i] = j
            break
        elif j == len(word)-1:
            alpha[i] = -1

print(*alpha)

"""
너무ㅅ 쉬운 난이도.
"""
