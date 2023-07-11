#문제 : 리스트에 문자열을 저장하고 출력	
#리스트 [] 선언, append 함수(내용 추가) 활용
#While문 내에서 입력 받기 : if 엔터( ‘ ‘ ) 누르면 정지
#리스트 컴프리핸션 전체 출력 : for문

array = [] #리스트 선언
while True: #while문, if 엔ㅌ 누르면 정지('')
    name = input('저장할 이름을 입력: ')
    if name == '':
        break
        array.append(name)

print('입력한 이름의 전체 목록: ')
for name in array:
    print(name, end = ',')