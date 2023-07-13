user_input = input('100글자 이내 소문자 문자열 1개 입력: ')
check = [-1]*26

for i in range(len(user_input)):
    index = ord(user_input[i]) - 97
    if check[index] == -1:
        check[index] = i
        
print('입력한 소문자의 위치를 표시:', check)