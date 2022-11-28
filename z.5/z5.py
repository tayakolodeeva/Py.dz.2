import datetime 

def get_rand():
    return datetime.datetime.now().microsecond%10
n = get_rand()
print(n)