import sys

case = int(sys.stdin.readline())
for _ in range(case):
    num = int(sys.stdin.readline())
    sumc = 0
    sumg = 0
    for _ in range(num):
        credit, grade = map(float, sys.stdin.readline().strip().split())
        sumg += grade * credit
        sumc += credit

    print("%d"%(sumc), end=' ')
    print("%.1f"%(sumg/sumc))
  
"""
힐링 문제..
"""
