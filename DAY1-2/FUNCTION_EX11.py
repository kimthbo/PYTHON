def av(*args):
    arr = [] #리스트 변수 선언
        for i in args:
        arr.append(i) # 매개변수를 각각 추가 저장
        
        temp = 0
        for j in arr:
            temp += j # temp에 합한 결과를 누적
        
        return temp/len(arr) # 평균 계산 리턴
        
print('입력한 정수의 평균을 출력: ', avg(1, 2, 2, 2, 2, 2, 3, 3, 4, 5))
