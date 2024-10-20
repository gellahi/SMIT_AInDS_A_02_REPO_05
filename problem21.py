size = 7
for i in range(size, 0, -1):
    for j in range(size - i):
        print(' ', end='')
    for k in range(i):
        print('*', end=' ')
    print()