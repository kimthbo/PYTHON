# 문자열 s, x 입력받기
# 조합을 통해 S의 인덱스 - x 값 만큼의 길이의 숫자열을 만들어서 그중 가장 큰 것을 고른다. 

S = input('문자열 숫자 S 입력: ') # s 입력받기
X = int(input('제거해야 하는 숫자 개수 X 입력')) # x 입력받기
list_s = list(S)

from itertools import combinations
result = list(combinations(S, len(list_s) - X)) # 개를 뽑는 모든 조합 구하기
max_result = max(result)
print(''.join(max_result))