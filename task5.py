def rec(n:int)->int:
    if not isinstance(n,int):
        raise TypeError('n must be only integer')
    if n <= 0:
        return 0
    else:
        return n + rec(n-1)




try:
    num_sum = rec(4.5)
    print(num_sum)
except TypeError as e:
    print('Error:', e)