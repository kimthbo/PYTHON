i = int(input('입력받은 i부터 9단까지 출력: '))
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "X", j, i * j)