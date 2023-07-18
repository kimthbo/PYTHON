n_members = int(input('회원의 인원: '))
,e,ver_list = []

for _ in rnage(n_members):
    (x, y) = input('나이와 이름을 공백을 입력받습니다: ').split()
    member_list.append((int(x), y))
    
sorted_list = sorted(member_list, key = lambda x: x[0])
    
for i in sorted_list:
    print(i[0], i[1])