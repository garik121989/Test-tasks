def func(st: str) -> dict:
    my_dict = {}
    if not isinstance(st,str):
        return "Error: 'st' can be only string"
    else:
        for i in st:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        return my_dict

print(func(5))