f_path = '/2020年11月前/test.txt'


def r_f():
    with open(f_path, "r", encoding='utf-8') as f:
        print(f.read())


def w_f():
    with open(f_path, "w", encoding='utf-8') as f:
        f.write('2020年11月前')


def a_f():
    with open(f_path, "a", encoding='utf-8') as f:
        f.write('\n' + 'hello world!')


w_f()
r_f()
a_f()
r_f()
