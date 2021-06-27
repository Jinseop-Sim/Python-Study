message = """
1. Coke 10$
2. Coffee 5$
3. Welchi's 10$
4. I don't need any drink

Which Drink you want? : 
"""
num = 0
money = 100
coke = 5
coffee = 5
welc = 5

while num != 4:
    print(message)
    num = eval(input())
    if(num > 4):
        print("I dunno what's that mean :<")
    if(money < 0):
        print("You don't have any money .. :(")
        break;
    if(num == 1):
        if (coke == 0):
            print("There's no coke :(")
        else:
            coke -= 1
            money -= 10
            print("Rest of coke is %d" %coke)
    elif(num == 2):
        if(coffee == 0):
            print("There is no Coffee :(")
        else:
            coffee -= 1
            money -= 5
            print("Rest of coffee is %d" %coffee)
    elif(num == 3):
        if(welc == 0):
            print("There is no Welchi's :(")
        else:
            welc -= 1
            money -= 10
            print("Rest of Welchi's is %d" %welc)

print("Good bye!")

```
python에서의 while문과 if문의 응용을 위해 간단하게 만들어본 자판기.
```
