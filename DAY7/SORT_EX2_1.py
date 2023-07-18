n = int(input('자연수의 개수 n 입력: ')) # N 입력 받기
a= []

for i in range(n):
    i = int(input('자연수 입력: '))
    a.append(i)
    
a.sort(reverse = True)
print(a)