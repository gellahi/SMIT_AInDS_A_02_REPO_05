size = 7
for i in range(size):
    for k in range(size - i -1):
        print(' ',end=' ')
    for j in range(size):
        if 0 < i < size - 1:
            if 0 < j < size - 1:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        else:
            print('*', end=' ')
    print()
