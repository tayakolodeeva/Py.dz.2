# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите N:'))
factorial = 1

print(end= '[ ')

for i in range(1, n+1):
    factorial *= i
    print(factorial, end=' ')

print(']')