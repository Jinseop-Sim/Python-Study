num = int(input())
rope = []
for _ in range(num):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(num):
    rope[i] = rope[i]*(i+1)

rope.sort(reverse=True)
print(rope[0])

"""
간단한 그리디 문제이다.
왜 그리디인가?
로프의 갯수가 바뀔 때 마다 최소 무게인 로프가 해가 되므로, 그리디 알고리즘이다.
"""
