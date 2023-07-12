import time
import os
import psutil 

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

n = 104195125111234124 
k = 4
result = 0
while True:
    target = (n // k) * k # K로 나눠지는 수를 구함, 예) 25 나누기 4 곱하기 4 = 처음 24
    result += (n - target) #n이 k 로 나누어 떨어지는 수가 될 때까지 빼기, 1
    n = target #24 -> 24 수정
    if n < k:
        break
    result += 1 # 계산 횟수 증가
    n //= k #kㄹ 나누기, n = 6
result += (n - 1) #마지막으로 남은 수에 대하여 1씩 빼기, 6, 5 -->6일때까지 2번 추가 빼기, 마지막 1번 나누고

print('1이 도달하기까지 연산 횟수: ', result) #총 5번 횟수 연산

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력