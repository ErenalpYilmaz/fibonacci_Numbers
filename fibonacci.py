#1,1,2,3,5,8,13,21,34 diye gider Fibonacci sayilari
#Kendinden bir onceki rakam ile toplanir sonraki rakam olarak yazilir.


choise = int(input("Kac adet fibonacci rakami gormek istiyorsunuz ? :"))


def fibonacci(choise):
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1
    print(1)
    while count < choise:
        print(next_number)
        count += 1
        num1 , num2 = num2 , next_number
        next_number = num1+num2




fibonacci(choise)