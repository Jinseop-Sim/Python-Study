wo1 = list(input())
wo2 = list(input())

dp = [[0]*(len(wo2)+1) for _ in range(len(wo1)+1)]

for i in range(len(wo1)):
    for j in range(len(wo2)):
        if wo1[i] == wo2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[len(wo1)][len(wo2)])

"""
어렵다.. DP문제..
LCS(Longest Common Sequence)이다.

단계별로 나눠서 생각해보도록하자.
문자열은 ACAYKP, CAPCAK 두 개로 주어진다.

1. wo1 문자열이 A일 때, 
   wo2 문자열이 C이면 LCS는 0이다.
   
   wo1 문자열이 A일 때,
   wo2 문자열이 CA이면, LCS는 1이다. ==> 최근에 추가되는 문자가 동일하면 +1을 해야한다!
   
   wo1 문자열이 A일 때,
   wo2 문자열이 CAP이면, LCS는 1이다.
   
   이런 식으로 CAPCAK까지 반복.

2. wo1 문자열이 AC일 때,
   wo2 문자열이 C이면 LCS는 1이다.
   
   wo1 문자열이 AC일 때
   wo2 문자열이 CA이면 LCS는 1이다.
   
   wo1 문자열이 AC일 때
   wo2 문자열이 CAP이면 LCS는 1이다. ==> 최근에 추가되는 문자열이 다른 경우, 이전 단계의 LCS 길이들 중 최대 값으로 가져온다.
   
   wo1 문자열이 AC일 때
   wo2 문자열이 CAPC 이면 LCS는 2이다. ==> 최근에 추가되는 문자가 동일하면 +1을 해준다!
   
3. 위와 같은 단계가 반복되면
   dp 배열에 데이터가 쌓이고 쌓여 최대 길이의 LCS를 찾을 수 있다.
