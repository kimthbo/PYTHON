import time
import os
import psutil

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

n, k = map(int,input('두 수를 공백으로 분리하여 입력: ').split()) # N = 동전의 종류 개수, K = 가격

input_lst = [] # 동전가격 리스트를 선언
while True:
    Ai = input('동전 가격을 오름차순으로 입력: ') #오름차순으로 동전가격을 입력받음
    if Ai == '': #동전가격을 다 넣었으면 enter를 눌러 다음으로 넘어감
        break
    input_lst.append(Ai)
Ai.sorting(reverse = True) #내림차순으로 동전가격을 정렬

count = 0
for coin in input_lst:
    if k < Ai:
        continue # 동전이 가격보다 크면 넘어감
    else:
        count += k // coin # 크지 않다면 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    
n %= coin
print('동전의 거스름돈 최소 개수는 :', count) # 개수 결과 출력

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력
