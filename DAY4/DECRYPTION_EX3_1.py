data = input('암호화된 문장을 공백으로 구분 입력: ')
value = ['a', 'e', 'i', 'o', 'u']
number = 0

while number < len(data):
    print(data[number], end='')
    if data[number] in value:
        number += 2
        number += 1