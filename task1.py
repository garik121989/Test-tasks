from typing import List, Any


def is_prime(n:int)->bool:
    if n == 2:
        return True
    elif n <= 0:
        return False
    elif  n == 1:
        return False
    else:
        for i in range(2, round(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def prime_num(n:int)->list:
    prime_list = []
    if not isinstance(n,int):
        return "'n' must be only integer"
    elif n == 1:
        return '1 is not prime'
    elif n <= 0:
        return "'n' can not be negative or zero"


    for i in range(2, n):
        if is_prime(i):
            prime_list.append(i)
    if prime_list == []:
        return 'there are no prime numbers in given range'
    else:
        return prime_list






res = prime_num(4)
print(res)



