# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
n = int(input('Введите N:'))
n_list = {}

for i in range(1, n+1):
    n_list[i] = round((1+1/i)**i, 3)
    
res = sum(n_list.values())
print(f'{n_list} сумма -> {res}')