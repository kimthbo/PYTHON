id_num = input('주민등록번호를 입력하세요: ')

if len(id_num) != 14:
    print('주민등록 번호 에러!')
    
gender = id_num[7]
region = id_num[8:10]
year = id_num[0:2]
month = id_num[2:4]
day = id_num[4:6]
    
int_month = int(month)
int_day = int(day)
int_gender = int(gender)
int_region = int(region)
    
if int_month >= 13 :
    print("주민등록 번호 에러!")
    
if int_day >= 32:
    print("주민등록 번호 에러!")
    
if int_gender >= 5:
    print("주민등록 번호 에러!")
    
else:
    if gender == 1 or gender == 2:
        year = "19" + year
    elif gender == 3 or gender == 4:
        year = "20" + year
    print('올바른 주민등록번호입니다.\n'
          '생년월일 :', year, '년', month, '월',  day, '일\n')
    if gender == 1 or gender == 3:
        print("성별 : 남성\n")    
    elif gender == 2 or gender == 4:
        print("성별 : 여성\n")
    if int_region >= 0 and 8 >= int_region:
        print('거주지 : 서울')
    if int_region >= 9 and 12 >= int_region:
        print('거주지 : 부산')
    if int_region >= 13 and 15 >= int_region:
        print('거주지 : 인천')
    if int_region >= 16 and 25 >= int_region:
        print('거주지 : 경기도')
    if int_region >= 26 and 34 >= int_region:
        print('거주지 : 강원도')
    if int_region >= 35 and 39 >= int_region:
        print('거주지 : 충청북도')
    if int_region == 40:
        print('거주지 : 대전')
    if int_region >= 41 and 47 >= int_region:
        print('거주지 : 충청남도')
    if int_region >= 48 and 54 >= int_region:
        print('거주지 : 전라북도')
    if int_region >= 55 and 66 >= int_region:
        print('거주지 : 전라남도')
    if int_region >= 55 and 56 >= int_region:
        print('거주지 : 광주')
    if int_region >= 67 and 69 >= int_region:
        print('거주지 : 대구')
    if int_region >= 70 and 75 >= int_region:
        print('거주지 : 경상북도')
    if int_region >= 77 and 81 >= int_region:
        print('거주지 : 경상남도')
    if int_region >= 82 and 84 >= int_region:
        print('거주지 : 울산광역시')
    if int_region == 85:
        print('거주지 : 제주특별시')
    if int_region >= 93 and 95 >= int_region:
        print('거주지 : 세종특별시')