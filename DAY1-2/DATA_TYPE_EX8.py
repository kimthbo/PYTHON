tuple_a = ()
input_lst = []
while Treu:
    name = input('저장할 이름을 입력: ')
    if name == '':
        break
        input_lst.append(name)
        
print('입력한 이름의 전체 목록: ')
for name in input_lst:
    print(name. end',')
    
    print('튜플로 캐스팅 후 출력: ')
    tuple_a = tuple(input_lst)
    print(tuple_a)