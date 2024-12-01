
def is_prime (func):
    def wrapper(*args, ** kwargs):
        res = func(*args, **kwargs)
        k = 0
        for i in range (int(res)):
            if res > 2 and res % (i+1) ==0:
                k+=1
        if k <3:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper

@is_prime
def sum_three (*args):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)
