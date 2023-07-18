from bisect import bisect_left, bisect_right

def count_by_x(array, x):
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)
    return right_index - left_index  # 특정 값의 개수 반환


n, x = map(int, input('정수 n가 x를 고백을 기준으로 구분하여 입력: ').split())
array = list(map(int, input('수열을 공백을 기준으로 구분하여 입력: ').split()))

# 특정 값의 개수를 세고 출력한다.
count = count_by_x(array, x)
if count <= 0:
    print(-1)
else:
    print(format(count))
