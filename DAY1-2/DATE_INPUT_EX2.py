s = input('주민등록번호를 입력해주세요.').split('-')
print(s)
print(''.join(s))

print(''.join(input('주민등록번호를 입력해주세요, -으로 구분: ').split('-'))) #주민번호에서 - 삭제하교 출력