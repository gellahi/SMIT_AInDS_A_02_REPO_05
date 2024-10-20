size = 7
for i in range(size):
    for j in range(i + 1):
        if 1 < i < size - 1:
            if 0 < j < i:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        else:
            print('*', end=' ')
    print()