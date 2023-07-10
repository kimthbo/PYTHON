n=int(input('1~100사이 정수를 입력하여 짝수만 출력:'))
sum = 0
for i in range(n+1):
    if(i % 2 == 0):
        sum += i
 print(sum)

while True:
    x=input('q 문자를 입력하면 프로그램 종료')
    print(x)
    if x == 'q':
        break
