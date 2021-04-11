def z():
    for i in range(1, 10):
        for j in range(1, i + 1):
            # print('%d×%d=%d' %(j, i, i*j), end='\t')
            # print('{}×{}={}'.format(j, i, i*j), end='\t')
            print(f'{i}×{j}={i * j}', end='\t')
        print()


def l_1():
    for i in range(9, 0, -1):
        for j in range(1, i + 1):
            # print('%d×%d=%d' %(j, i, i*j), end='\t')
            # print('{}×{}={}'.format(j, i, i*j), end='\t')
            print(f'{i}×{j}={i * j}', end='\t')
        print()


def l_2():
    for i in range(8, 0, -1):
        for j in range(1, i + 1):
            # print('%d×%d=%d' %(j, i, i*j), end='\t')
            # print('{}×{}={}'.format(j, i, i*j), end='\t')
            print(f'{i}×{j}={i * j}', end='\t')
        print()


z()
l_2()
