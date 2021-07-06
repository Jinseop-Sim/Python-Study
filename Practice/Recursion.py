def pick(n, prev, next):
    if next == 0:
        print(prev)
        return

    if not prev:
        small = 0
    else:
        small = prev[-1] + 1

    for i in range(small, n):
        prev.append(i)
        pick(n, prev, next-1)
        prev.pop(-1)

print(pick(7,[],4))

"""
재귀 호출을 이용한 조합을 연습한 것이다.
n개중에 4개를 중복 없이 뽑는 경우이다.
원래라면 반복문을 4개 만들어서 O(N^4)의 시간복잡도를 가지겠지만, 이렇게 재귀로 하면
시간 복잡도를 대폭 감소시킬 수 있다.
"""
