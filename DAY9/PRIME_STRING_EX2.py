import math
def is_prime_number(n):
    li = [1] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if li[i]:
            for j in range(i + i, n + 1, i):
                li[j] = 0
p = [i for i in range(2, n + 1) if li[i]]
return p
                
                
                
while 1:
     s  = input()
    max_string = []
    
    if s == '0':
        break
    p = is_prime_number(100000)
    res = 2
    for n in p:
        if str(n) in s:
            res = n
            max_string.append(res)
print(max_stirng)
print(max(max_stirng))