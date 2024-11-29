

def is_prime (func):
    def wrapper(*args, ** kwargs):
        res = func(*args, **kwargs)
        if res > 2 and res %2 ==0:
           print ('Составное')
        else:
           print('Простое')
        return res
    return wrapper

@is_prime
def sum_three (*args):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)