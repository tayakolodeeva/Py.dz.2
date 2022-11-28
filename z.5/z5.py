import datetime 

min_n = (input('Введите диапазон от :'))
max_n = (input('до :'))

def get_rand():
    return datetime.datetime.now().microsecond%10

n = get_rand()

print(int(len(str(min_n))))
print(n)