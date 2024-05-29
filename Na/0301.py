# 현재 상황에서 지금 당장 좋은 것만 고르는 방법 - 그리디
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # 해당 화페로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
