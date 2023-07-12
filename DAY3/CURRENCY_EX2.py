import time
import os
import psutil

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

n, k = map(int, input('동전 가격을 개수만큼 입력: ').split()) # N = 동전의 종류 개수, K = 가격
coins = [] # 동전가격 리스트를 선언
    coins.append(int(input('동전 가격을 오름차순으로 입력: '))) #오름차순으로 동전가격을 입력받음
coins.sorting(reverse = True) #내림차순으로 동전가격을 정렬

count = 0
for coin in coins:
    if k >= coin:
        count += k // coin # 크지 않다면 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
        k %= coin
        if k <= 0
            break
print('동전의 거스름돈 최소 개수는 :', count) # 개수 결과 출력

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력
