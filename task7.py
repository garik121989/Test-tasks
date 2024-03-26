def foo(a: str, b: str,  file):
    replaced_txt = file.replace(a, b)
    with open('/home/garik/text2.txt', 'w') as text2:
        text2.write(replaced_txt)


try:
    with open('/home/garik/data.tat', 'r') as f:
        file_txt = f.read()
        foo('a', 'l', file_txt)
except FileNotFoundError:
    print('Error: file not found')
