def foo(n: int) -> bool:
    if not isinstance(n, int):
        return "Error: 'n' can be only integer"
    else:
        if n != 0 and (abs(n) & (abs(n) - 1)) == 0:
            return True
        return False


print(foo(-8))
