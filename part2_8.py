def divisible_by_two(number):
    return number 
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num2 = num2 + 1
diapazon = range(num1, num2)
result = filter(divisible_by_two, diapazon)
print(list(result))
