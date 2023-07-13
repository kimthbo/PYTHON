array = [-1] * 26
str_s = input('소문자 단어를 입력: ')

for i in range(len(str_s)):
    index_s = int(ord(str_s[0])) - int(ord('a'))
    if array[index_s] = -1:
        array[index_s] = i

print(array)