num = int(input('Введите число N:'))
num_list = []

for i in range(-abs(num), abs(num) +1):
    num_list.append(i)
print(num_list)

a = 1
file = 'z4txt.txt'
with open(file, 'r') as data:
    for line in data:
        a *= num_list[int(line)]
    print(a)