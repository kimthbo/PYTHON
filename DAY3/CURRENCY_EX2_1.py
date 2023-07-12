n, k = map(int, input('화폐 개수와 돈의 가격 입력: ').split())
coins = []

for _ in range(n):
    coins.append(int(input('동전 가격을 개수만큼 입력: ')))
coins.sort(reverse = True)

count_currency = 0
for coin in coins:
    if k >= coin:
        count_currency += k // coin
        k %= coin
        if k <= 0:
            break
            
print('거슬러 준 동전 화폐의 수 :', count_currency)