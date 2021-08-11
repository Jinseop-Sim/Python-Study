fix, prod, sell = map(int, input().split())

if(sell <= prod):
    print(-1)
if(sell > prod):
    bep = fix // (sell - prod) + 1
    print(bep)
    
```
간단하게 손익 분기점(Break-Even Point)를 구하는 문제.
물론 실제 경제는 다르겠지만, 이 문제에서는 (고정가격 // (판매가격 - 생산단가)) + 1 을 하면 간단히 도출이 된다.
다만 DivideByZero 에러를 피하기 위해 sell = prod가 되는 경우에도 -1을 출력하고 프로그램을 종료하도록 한다.
```
