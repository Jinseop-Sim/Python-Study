def calc(num, idx, add, sub, multi, division):
    global n, maxv, minv
    if idx == n:
        print(num)
        maxv = max(num, maxv)
        minv = min(num, minv)
        return
    else:
        if add:
            calc(num+num_list[idx], idx+1, add-1, sub, multi, division)
        if sub:
            calc(num-num_list[idx], idx+1, add, sub-1, multi, division)
        if multi:
            calc(num*num_list[idx], idx+1, add, sub, multi-1, division)
        if division:
            calc(int(num/num_list[idx]), idx+1, add, sub, multi, division-1)

maxv = -1000000000
minv = 1000000000
n = int(input())
num_list = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
calc(num_list[0], 1, a, b, c, d)
print(maxv)
print(minv)

"""
연산자 끼워넣기의 반복문이 아닌 재귀식 풀이이다.
calc 함수 내의 else문 내의 if문들을 if~else문이 아닌 if문들로 놔둔 이유는, 모든 경우를 탐색하기 위해서이다.
만약 elif로 묶어버리면, add => add => sub => multi => division 이 한 가지 경우 밖에 작동하지 않는다.
if문으로 묶는다면, 제일 첫 반복문에서 2 1 1 1의 배열로 넘어왔다고 가정한다면
add(1) => add(0) => sub(0) => multi(0) => div (0)
                           => div(0) => multi(0)
                 => multi(0)
                 => div(0)
       => sub(0) => add(0)   ..
                 => multi(0)
                 => div(0)
       => multi(0) => add(0)
                   => multi(0)
                   => div(0)
       => division(0) => add(0)
                      => sub(0)
                      => multi(0)

대략 이런식의 DFS(Depth-First Searching)이 진행이 된다.
"""
