# sort

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1.sort()

l1.sort(reverse=True)


# 우선순위 지정 정렬
# <list>.sort(key=<function>, reverse=<bool>)

# 두번째 데이터(x[1])을 기준으로 오름차순 정렬
l3 = [[1, 2], [5, 3], [3, 7], [7, 4], [6, 1]]
l3.sort(key=lambda x: -x[1])
