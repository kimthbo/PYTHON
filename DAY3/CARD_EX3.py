n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split())) #한 줄 씩 입력받아 확인
    min_value = min(data) #현재줄에서 가장 작은 수 차기
    result = max(result, min_value) #'가장 작은 수' 들 중에서 가장 큰 수 찾기
    print(result)